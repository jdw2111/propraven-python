"""Auto-pagination helpers used by the generated ``*_iter`` methods."""

from __future__ import annotations

from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, List, Optional, Tuple

__all__ = ["iterate_offset", "aiterate_offset", "iterate_cursor", "aiterate_cursor"]


def _items(page: Any, key: str) -> List[Any]:
    if isinstance(page, list):
        return page
    if isinstance(page, dict):
        items = page.get(key)
        if isinstance(items, list):
            return items
    return []


def _number(value: Any) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def _offset_next(page: Any, n: int, offset: int, requested_limit: Optional[int]) -> Optional[int]:
    """Return the next offset, or ``None`` when ``page`` was the last page."""
    if n == 0:
        return None
    if isinstance(page, dict):
        has_more = page.get("has_more")
        if isinstance(has_more, bool):
            return offset + n if has_more else None
        total = _number(page.get("total"))
        if total is not None and not page.get("total_is_estimate") and not page.get("total_is_lower_bound"):
            if offset + n >= total:
                return None
        echoed = _number(page.get("limit"))
        limit = int(echoed) if echoed is not None and echoed > 0 else requested_limit
    else:
        limit = requested_limit
    if limit is not None and n < limit:
        return None
    return offset + n


def _take(items: List[Any], yielded: int, max_items: Optional[int]) -> Tuple[List[Any], bool]:
    if max_items is None:
        return items, False
    room = max_items - yielded
    if room <= 0:
        return [], True
    if len(items) >= room:
        return items[:room], True
    return items, False


def iterate_offset(
    fetch: Callable[[Optional[int], int], Any],
    *,
    items: str,
    page_size: Optional[int] = None,
    max_items: Optional[int] = None,
    start_offset: int = 0,
) -> Iterator[Any]:
    """Yield items across offset pages. ``fetch(limit, offset)`` returns one page.

    Stops on an empty or short page, when ``offset >= total`` (``total`` a number),
    when ``has_more`` is false, or after ``max_items`` items.
    """
    offset = start_offset
    yielded = 0
    if max_items is not None and max_items <= 0:
        return
    while True:
        page = fetch(page_size, offset)
        rows = _items(page, items)
        chunk, done = _take(rows, yielded, max_items)
        yield from chunk
        yielded += len(chunk)
        if done:
            return
        nxt = _offset_next(page, len(rows), offset, page_size)
        if nxt is None:
            return
        offset = nxt


async def aiterate_offset(
    fetch: Callable[[Optional[int], int], Awaitable[Any]],
    *,
    items: str,
    page_size: Optional[int] = None,
    max_items: Optional[int] = None,
    start_offset: int = 0,
) -> AsyncIterator[Any]:
    """Async version of :func:`iterate_offset`."""
    offset = start_offset
    yielded = 0
    if max_items is not None and max_items <= 0:
        return
    while True:
        page = await fetch(page_size, offset)
        rows = _items(page, items)
        chunk, done = _take(rows, yielded, max_items)
        for row in chunk:
            yield row
        yielded += len(chunk)
        if done:
            return
        nxt = _offset_next(page, len(rows), offset, page_size)
        if nxt is None:
            return
        offset = nxt


def _cursor_next(page: Any, next_key: str, previous: Optional[str]) -> Optional[str]:
    if not isinstance(page, dict):
        return None
    if page.get("hasMore") is False or page.get("has_more") is False:
        return None
    cursor = page.get(next_key)
    if cursor is None or cursor == "" or cursor == previous:
        return None
    return str(cursor)


def iterate_cursor(
    fetch: Callable[[Optional[int], Optional[str]], Any],
    *,
    items: str,
    next_key: str,
    page_size: Optional[int] = None,
    max_items: Optional[int] = None,
) -> Iterator[Any]:
    """Yield items across cursor pages. ``fetch(limit, cursor)`` returns one page; the
    next cursor is ``page[next_key]``; stops when it is null/absent or ``hasMore`` is false."""
    cursor: Optional[str] = None
    yielded = 0
    if max_items is not None and max_items <= 0:
        return
    while True:
        page = fetch(page_size, cursor)
        rows = _items(page, items)
        chunk, done = _take(rows, yielded, max_items)
        yield from chunk
        yielded += len(chunk)
        if done or not rows:
            return
        cursor = _cursor_next(page, next_key, cursor)
        if cursor is None:
            return


async def aiterate_cursor(
    fetch: Callable[[Optional[int], Optional[str]], Awaitable[Any]],
    *,
    items: str,
    next_key: str,
    page_size: Optional[int] = None,
    max_items: Optional[int] = None,
) -> AsyncIterator[Any]:
    """Async version of :func:`iterate_cursor`."""
    cursor: Optional[str] = None
    yielded = 0
    if max_items is not None and max_items <= 0:
        return
    while True:
        page = await fetch(page_size, cursor)
        rows = _items(page, items)
        chunk, done = _take(rows, yielded, max_items)
        for row in chunk:
            yield row
        yielded += len(chunk)
        if done or not rows:
            return
        cursor = _cursor_next(page, next_key, cursor)
        if cursor is None:
            return
