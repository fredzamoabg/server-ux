# Copyright (C) 2020 - Iván Todorovich <ivan.todorovich@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade


def uninstall_mass_editing(env):
    mass_editing = env['ir.module.module'].search([('name', '=', 'mass_editing')])
    if mass_editing:
        mass_editing.module_uninstall()


@openupgrade.migrate()
def migrate(env, version):
    uninstall_mass_editing(env)
