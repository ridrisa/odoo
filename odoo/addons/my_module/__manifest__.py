{
    'name': 'My Module',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'Module for Courier Master Sheet Management',
    'description': """
        Module to manage Courier Master Sheets.
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/courier_master_sheet_views.xml',
    ],
    'installable': True,
    'application': True,
}
