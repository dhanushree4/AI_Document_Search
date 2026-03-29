import reflex as rx

config = rx.Config(
    app_name="RAG_PROJECT",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)
