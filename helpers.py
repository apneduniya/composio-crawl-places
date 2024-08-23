import json
import typing as t


def parse_json_garbage(s: str) -> t.Dict[str, t.Any]:
    """
    This function converts string containing json to a json object.

    @param s: str - The string to parse.
    @return: t.Dict[str, t.Any] - The parsed json garbage.
    """
    s = s[next(idx for idx, c in enumerate(s) if c in "{["):]
    try:
        return json.loads(s)
    except json.JSONDecodeError as e:
        return json.loads(s[:e.pos])