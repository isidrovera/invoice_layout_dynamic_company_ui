# -*- coding: utf-8 -*-

from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    # Brand Colors
    report_brand_color = fields.Char(
        string='Brand Color (Primary)',
        help='Main brand color for header wave (e.g., #1F6FEB)',
        default='#1F6FEB'
    )
    
    report_accent_color = fields.Char(
        string='Accent Color (Secondary)',
        help='Secondary brand color for footer wave (e.g., #0B3D91)',
        default='#0B3D91'
    )
    
    # Opacity Controls
    report_header_opacity = fields.Float(
        string='Header Wave Opacity',
        help='Opacity of the header wave (0.0 to 1.0)',
        default=0.18,
    )
    
    report_footer_opacity = fields.Float(
        string='Footer Wave Opacity',
        help='Opacity of the footer wave (0.0 to 1.0)',
        default=0.22,
    )
    
    # Logo Settings
    report_logo_max_height = fields.Integer(
        string='Logo Max Height (px)',
        help='Maximum height for company logo in reports',
        default=88,
    )
    
    # Design Settings
    report_radius = fields.Integer(
        string='Border Radius (px)',
        help='Border radius for rounded elements',
        default=12,
    )
    
    report_head_bg_alpha = fields.Float(
        string='Table Header Background Opacity',
        help='Opacity for table headers (0.0 to 1.0)',
        default=0.06,
    )
    
    # Typography
    report_font_size = fields.Selection([
        ('small', 'Small (11px)'),
        ('medium', 'Medium (12px)'),
        ('large', 'Large (13px)'),
    ], string='Report Font Size', default='medium')
    
    # Layout Options
    report_header_height = fields.Integer(
        string='Header Height (px)',
        help='Height of the header wave',
        default=260,
    )
    
    report_show_tagline = fields.Boolean(
        string='Show Company Tagline',
        default=True,
    )
    
    report_modern_style = fields.Boolean(
        string='Enable Modern Style',
        help='Use modern design with shadows and rounded corners',
        default=True,
    )