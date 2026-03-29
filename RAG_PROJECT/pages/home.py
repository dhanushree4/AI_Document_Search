import reflex as rx
from RAG_PROJECT.components.navbar import navbar
from RAG_PROJECT.components.footer import footer


# 🌿 THEME
ACCENT = "#84cc16"
BG = "#020617"
CARD = "#0f172a"
BORDER = "#1f2937"
TEXT = "#e5e7eb"
SUBTEXT = "#9ca3af"


# 🔹 CONTAINER (FIXES ALIGNMENT ISSUE)
def container(content, **kwargs):
    return rx.box(
        content,
        max_width="1200px",
        margin="0 auto",
        width="100%",
        padding_x="30px",
        **kwargs,   # ✅ allows extra styles like padding_bottom
    )


# 🔹 CARD STYLE
def card_style():
    return {
        "transition": "all 0.3s ease",
        "_hover": {
            "transform": "translateY(-6px)",
            "border": f"1px solid {ACCENT}",
        },
    }


# 🔹 FEATURE CARD
def feature_card(icon, title, desc):
    return rx.box(
        rx.vstack(
            rx.text(icon, font_size="22px"),
            rx.text(title, color=TEXT, font_weight="700"),
            rx.text(desc, color=SUBTEXT, font_size="13px"),
            spacing="3",
            align="start",
        ),
        padding="24px",
        bg=CARD,
        border=f"1px solid {BORDER}",
        border_radius="14px",
        width="100%",
        style=card_style(),
    )


# 🔹 STEP CARD
def step_card(num, title, desc):
    return rx.box(
        rx.vstack(
            rx.text(num, color=ACCENT, font_weight="800"),
            rx.text(title, color=TEXT, font_weight="700"),
            rx.text(desc, color=SUBTEXT, font_size="13px"),
            spacing="2",
            align="start",
        ),
        padding="20px",
        bg=CARD,
        border=f"1px solid {BORDER}",
        border_radius="12px",
        style=card_style(),
    )


def home():
    return rx.box(
        navbar(),

        rx.vstack(

            # 🌿 HERO SECTION
            container(
                rx.vstack(
                    rx.text(
                        "AI DOCUMENT INTELLIGENCE",
                        color=ACCENT,
                        font_size="12px",
                        font_weight="600",
                        letter_spacing="0.15em",
                    ),

                    rx.heading(
                        "Turn Your Documents Into",
                        size="9",
                        color=TEXT,
                        text_align="center",
                    ),
                    rx.heading(
                        "Instant Answers",
                        size="9",
                        color=ACCENT,
                        text_align="center",
                    ),

                    rx.text(
                        "Upload your files, ask questions naturally, and get precise answers "
                        "grounded in your data. No searching, no scrolling — just clarity.",
                        color=SUBTEXT,
                        font_size="16px",
                        text_align="center",
                        max_width="650px",
                        line_height="1.7",
                    ),

                    rx.hstack(
                        rx.button(
                            "Upload Documents",
                            on_click=rx.redirect("/upload"),
                            bg=ACCENT,
                            color="black",
                            size="4",
                            border_radius="10px",
                            style={"_hover": {"transform": "scale(1.05)"}},
                        ),
                        rx.button(
                            "Start Chat",
                            on_click=rx.redirect("/chat"),
                            variant="outline",
                            size="4",
                        ),
                        spacing="4",
                        margin_top="20px",
                    ),

                    spacing="4",
                    align="center",
                    padding_y="80px",
                    style={"animation": "fadeIn 0.8s ease"},
                )
            ),

            # 🌿 WHY SECTION
            container(
                rx.vstack(
                    rx.heading("Why This System?", size="7", color=TEXT),

                    rx.text(
                        "Traditional search forces you to dig through documents manually. "
                        "Our system understands context, retrieves only what matters, and "
                        "generates meaningful answers instantly.",
                        color=SUBTEXT,
                        text_align="center",
                        max_width="700px",
                    ),

                    spacing="4",
                    align="center",
                    padding_bottom="50px",
                )
            ),

            # 🌿 FEATURES
            container(
                rx.grid(
                    feature_card("📄", "Smart Upload", "Automatically processes PDFs and text files."),
                    feature_card("🔍", "Context Search", "Finds meaning, not just keywords."),
                    feature_card("🧠", "AI Reasoning", "Answers generated using LLM intelligence."),
                    feature_card("⚡", "Fast Results", "Optimized with high-speed inference."),
                    columns="2",
                    spacing="5",
                    width="100%",
                    padding_bottom="70px",
                )
            ),

            # 🌿 USER FLOW
            container(
                rx.vstack(
                    rx.heading("How It Works", size="7", color=TEXT),

                    rx.grid(
                        step_card("1", "Upload", "Add your documents securely."),
                        step_card("2", "Process", "System extracts and understands content."),
                        step_card("3", "Retrieve", "Relevant context is identified."),
                        step_card("4", "Answer", "AI generates precise responses."),
                        columns="4",
                        spacing="4",
                    ),

                    spacing="5",
                    align="center",
                    padding_bottom="70px",
                )
            ),

            # 🌿 CTA SECTION
            container(
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "Start Exploring Your Data",
                            size="7",
                            color=TEXT,
                            text_align="center",
                        ),
                        rx.text(
                            "Upload your first document and experience intelligent search powered by AI.",
                            color=SUBTEXT,
                            text_align="center",
                        ),

                        rx.button(
                            "Get Started →",
                            on_click=rx.redirect("/upload"),
                            bg=ACCENT,
                            color="black",
                            size="4",
                            border_radius="10px",
                            margin_top="15px",
                        ),

                        spacing="4",
                        align="center",
                    ),
                    padding="50px",
                    bg=CARD,
                    border=f"1px solid {BORDER}",
                    border_radius="18px",
                    style={
                        "transition": "0.3s",
                        "_hover": {"transform": "scale(1.02)"},
                    },
                ),
                padding_bottom="80px",
            ),

        ),

        footer(),

        bg=f"linear-gradient(135deg, {BG}, #111827)",
        min_height="100vh",
    )