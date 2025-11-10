from odoo import fields, models

class ResCompany(models.Model):
    _inherit = "res.company"

    report_brand_color = fields.Char(string="Brand Color (HEX)",
                                     help="Override primary color for reports, e.g. #2A8CFF")
    report_accent_color = fields.Char(string="Accent/Secondary Color (HEX)")
    report_logo_max_height = fields.Integer(string="Logo Max Height (px)", default=88)
    report_header_opacity = fields.Float(string="Header Wave Opacity", default=0.18)
    report_footer_opacity = fields.Float(string="Footer Wave Opacity", default=0.22)
    report_radius = fields.Integer(string="Border Radius (px)", default=12)
    report_head_bg_alpha = fields.Float(string="Table Head Alpha (0-1)", default=0.04)