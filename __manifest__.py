{
    "name": "Invoice Layout – Dynamic (Odoo 19, Company UI)",
    "summary": "Dynamic colors, sizes and styles for Wave report layout (company-specific). Company form configuration UI.",
    "version": "19.0.1.0.1",
    "license": "OEEL-1",
    "author": "ChatGPT",
    "website": "https://example.com",
    "depends": ["web", "base", "account"],
    "assets": {
        "web.report_assets_common": [
            "invoice_layout_dynamic_company_ui/static/src/scss/invoice_layout.scss"
        ],
        "web.report_assets_pdf": [
            "invoice_layout_dynamic_company_ui/static/src/scss/invoice_layout.scss"
        ]
    },
    "data": [
        "views/res_company_view.xml",
        "views/external_layout_wave_inherit.xml"
    ],
    "installable": True,
    "application": False
}