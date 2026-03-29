import reflex as rx
def footer():
    return rx.box(
        rx.hstack(
            rx.text(
                "© 2026 DataTalk By Dhanushree — Powered by LangChain · Groq · ChromaDB",
                color="#4a5568",
                font_size="12px",
                letter_spacing="0.04em",
            ),
            rx.spacer(),
            rx.link(
                     rx.icon("linkedin", size=18, color="#64748b"),
                     href="https://www.linkedin.com/in/dhanushree-d-1334b625b/",
                     is_external=True,
                        ),
            rx.hstack(
                rx.box(width="6px", height="6px", border_radius="50%", bg="#84cc16",),
                rx.text("System Online", color="#4a5568", font_size="11px"),
                spacing="2",
                align="center",
            ),
            width="100%",
            padding_x="32px",
        ),
        width="100%",
        padding_y="14px",
        bg="#0a0c10",
        border_top="1px solid #1e2535",
        margin_top="auto",
    )
    
    
    