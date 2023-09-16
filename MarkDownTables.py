from dataclasses import dataclass


@dataclass
class MarkDownTables:
    table: str = ""

    @classmethod
    def create_table(cls, titles: list[dict], values: dict[dict[list[dict]]]):
        # Set up the table headers with their alignments
        alignments = {
            'left': ':---',
            'center': ':---:',
            'right': '---:',
        }
        headings = ''
        col_aligns = ''
        eol = '|\n'
        for title in titles:
            headings += f'| {title["title"]} '
            col_aligns += f'| {alignments.get(title["align"], alignments["center"])} '
        cls.table = headings + eol + col_aligns + eol

        # Get the column titles in order
        title_names = [title['name'] for title in titles]
        for env in values:
            # Set up the row with the environment name
            cls.table += f'| {env} '
            # Loop through the titles and get the value for the environment
            for title in title_names:
                if title == 'environment':
                    continue
                # Find the value for the title
                value = [item.get('value', '') for item in values.get(env) if item.get('name') == title]
                # Add the value to the table
                cls.table += f'| {value[0]} '
            # Add a new line to the table
            cls.table += eol
        return cls.table
