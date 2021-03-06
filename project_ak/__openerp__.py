# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2015-TODAY Akretion (http://www.akretion.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Project Akretion',
    'summary': 'Custom for Akretion',
    'version': '0.1',
    "category": "Project Management",
    'description': """\
This module extends the ``Project`` module to allow manage issues with tasks.
Please refer to that module's description.
""",
    'author': "Akretion, Odoo Community Association (OCA)",
    'website': '',
    'license': 'AGPL-3',
    'depends': [
        'project_milestone',
        'project_model_to_task',
    ],
    'data': [
        'project_data.xml',
        'security/group.xml',
        'project_view.xml',
        'wizard/invoice_work_view.xml',
    ],
    'installable': True,
    'application': True,
}
