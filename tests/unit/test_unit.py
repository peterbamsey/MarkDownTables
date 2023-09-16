import pytest

from MarkDownTables import MarkDownTables


class TestMarkDownTables:
    table: str

    def setUp(self):
        self.table = """| Environment | Company Backend App1 | Company Backend App2 | Company Frontend App1 | Company Frontend App2 |\n| :---: | :---: | :---: | :---: | :---: |\n| test1 | main | feature-1 | main | feature-2 |\n| test2 | main | main | main | main |\n| test3 | main | main | feature-3 | main |\n"""

    def test_create_table(self, titles, values):
        self.setUp()
        table = MarkDownTables().create_table(titles, values)
        assert table == self.table


@pytest.fixture
def titles():
    yield [
        {
            'name': 'environment',
            'title': 'Environment',
            'align': 'center',
        },
        {
            'name': 'company-backend-app1',
            'title': 'Company Backend App1',
            'align': 'center',
        },
        {
            'name': 'company-backend-app2',
            'title': 'Company Backend App2',
            'align': 'center',
        },
        {
            'name': 'company-frontend-app1',
            'title': 'Company Frontend App1',
            'align': 'center',
        },
        {
            'name': 'company-frontend-app2',
            'title': 'Company Frontend App2',
            'align': 'center',
        }
    ]


@pytest.fixture
def values():
    yield {
        'test1': [
            {
                'name': 'company-backend-app1',
                'value': 'main',
            },
            {
                'name': 'company-backend-app2',
                'value': 'feature-1',
            },
            {
                'name': 'company-frontend-app1',
                'value': 'main',
            },
            {
                'name': 'company-frontend-app2',
                'value': 'feature-2',
            }
        ],
        'test2': [
            {
                'name': 'company-backend-app1',
                'value': 'main',
            },
            {
                'name': 'company-backend-app2',
                'value': 'main',
            },
            {
                'name': 'company-frontend-app1',
                'value': 'main',
            },
            {
                'name': 'company-frontend-app2',
                'value': 'main',
            }
        ],
        'test3': [
            {
                'name': 'company-backend-app1',
                'value': 'main',
            },
            {
                'name': 'company-backend-app2',
                'value': 'main',
            },
            {
                'name': 'company-frontend-app1',
                'value': 'feature-3',
            },
            {
                'name': 'company-frontend-app2',
                'value': 'main',
            }
        ]
    }
