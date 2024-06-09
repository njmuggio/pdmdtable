def build_table(header: list[str], body: list[list[str]]) -> str:
    if len(header) == 0:
        raise TableDimensionError("Header must contain at least one column")

    col_widths = [0] * len(header)

    for idx in range(len(header)):
        header[idx] = str(header[idx])
        col_widths[idx] = __width(header[idx])

    for row in body:
        for col_idx in range(len(row)):
            row[col_idx] = str(row[col_idx])
            col_widths[col_idx] = max(col_widths[col_idx], __width(row[col_idx]))

    table = ""

    table += "+" + "+".join(("-" * (2 + width) for width in col_widths)) + "+\n"
    table += __build_row(col_widths, header)
    table += "+" + "+".join(("=" * (2 + width) for width in col_widths)) + "+\n"

    for idx, row in enumerate(body):
        table += __build_row(col_widths, row)
        if idx < len(body) - 1:
            table += "+" + "+".join(("-" * (2 + width) for width in col_widths)) + "+\n"

    table += "+" + "+".join(("-" * (2 + width) for width in col_widths)) + "+"

    return table


class TableDimensionError(ValueError):
    pass


def __width(s: str) -> int:
    return max((len(l) for l in s.splitlines()))


def __height(s: str) -> int:
    return len(s.splitlines())


def __build_row(widths: list[int], cells: list[str]) -> str:
    if not len(cells):
        return ""

    lines = [""] * max((__height(cell) for cell in cells))

    for cell_idx, cell_width in enumerate(widths):
        cell = cells[cell_idx] if cell_idx < len(cells) else ""

        #for line_idx in range(len(lines)):
        #    lines[line_idx] += "| "

        #for line_idx, line in enumerate(cell.splitlines()):
        #    lines[line_idx] += line.ljust(widths[cell_idx] + 1)
        cell_lines = cell.splitlines()
        for line_idx in range(len(lines)):
            lines[line_idx] += "| "
            if line_idx < len(cell_lines):
                lines[line_idx] += cell_lines[line_idx].ljust(widths[cell_idx] + 1)
            else:
                lines[line_idx] += " " * (widths[cell_idx] + 1)

    for line_idx in range(len(lines)):
        lines[line_idx] += "|\n"

    return "".join(lines)
