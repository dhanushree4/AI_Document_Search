import reflex as rx


def hero():
    return rx.vstack(

        # ── HERO MAIN ─────────────────────────────
        rx.box(
            rx.vstack(

                # Badge
                rx.box(
                    rx.hstack(
                        rx.box(
                            width="6px",
                            height="6px",
                            bg="#84cc16",
                            border_radius="50%",
                        ),
                        rx.text(
                            "AI DOCUMENT INTELLIGENCE",
                            color="#84cc16",
                            font_size="11px",
                            font_weight="700",
                            letter_spacing="0.2em",
                        ),
                        spacing="2",
                        align="center",
                    ),
                    padding_x="14px",
                    padding_y="6px",
                    border="1px solid rgba(132,204,22,0.3)",
                    border_radius="20px",
                    background="rgba(132,204,22,0.05)",

                    # animation
                    style={"animation": "fadeIn 0.8s ease"},
                ),

                # Heading
                rx.heading(
                    rx.text.span(
                        "Smart Document Intelligence",
                        color="#f1f5f9"
                    ),
                    rx.text.span(
                        "\nPowered by AI Retrieval",
                        color="#84cc16"
                    ),
                    size="9",
                    text_align="center",
                    line_height="1.2",
                    style={
                        "font_size": "clamp(2.8rem, 5vw, 4rem)",
                        "letter_spacing": "-1px",
                        "animation": "fadeInUp 0.9s ease"
                    }
                ),

                # Description
                rx.text(
                    "Upload your documents, ask questions naturally, and get precise answers "
                    "powered by Retrieval-Augmented Generation with intelligent context understanding.",
                    color="#94a3b8",
                    font_size="18px",
                    text_align="center",
                    max_width="650px",
                    line_height="1.8",

                    style={"animation": "fadeInUp 1s ease"}
                ),

                # Buttons
                rx.hstack(
                    rx.button(
                        "Upload Documents",
                        rx.icon(tag="upload", size=18),
                        on_click=rx.redirect("/upload"),

                        background="#84cc16",
                        color="#0b0f19",
                        font_weight="700",
                        padding_x="28px",
                        padding_y="18px",
                        border_radius="10px",

                        box_shadow="0 10px 30px rgba(132,204,22,0.3)",

                        _hover={
                            "background": "#65a30d",
                            "transform": "translateY(-3px) scale(1.03)",
                            "box_shadow": "0 20px 40px rgba(132,204,22,0.4)"
                        },
                        transition="all 0.25s ease",
                    ),

                    rx.button(
                        "Start Chat",
                        on_click=rx.redirect("/chat"),

                        background="transparent",
                        color="#e2e8f0",
                        border="1px solid rgba(132,204,22,0.3)",
                        padding_x="28px",
                        padding_y="18px",
                        border_radius="10px",

                        _hover={
                            "color": "#84cc16",
                            "border_color": "#84cc16",
                            "transform": "translateY(-2px)"
                        },
                        transition="all 0.25s ease",
                    ),

                    spacing="4",
                ),

                spacing="6",
                align="center",
            ),

            display="flex",
            justify_content="center",
            width="100%",
            padding_y="100px",

            # subtle glow background
            background="radial-gradient(circle at top, rgba(132,204,22,0.08), transparent 70%)",
        ),

        # ── FEATURE CARDS ─────────────────────────
        rx.hstack(
            feature_card("⚡", "Fast Retrieval", "Sub-second semantic search using embeddings"),
            feature_card("🔒", "Secure Processing", "Local vector store with private document access"),
            feature_card("🧠", "AI Understanding", "Context-aware answers using RAG pipeline"),

            spacing="6",
            justify="center",
            wrap="wrap",
            margin_top="40px",
        ),

        width="100%",
        min_height="85vh",
        align="center",

        # dark theme background
        background="linear-gradient(180deg, #080a0f, #0f172a)",
    )


# ── FEATURE CARD ─────────────────────────────
def feature_card(icon, title, description):
    return rx.vstack(
        rx.text(icon, font_size="26px"),

        rx.text(
            title,
            font_weight="700",
            font_size="17px",
            color="#e2e8f0"
        ),

        rx.text(
            description,
            color="#94a3b8",
            font_size="14px",
            text_align="center"
        ),

        align="center",
        padding="24px",
        background="#0f172a",
        border="1px solid rgba(132,204,22,0.15)",
        border_radius="16px",
        width="260px",

        box_shadow="0 4px 20px rgba(0,0,0,0.2)",

        # 🔥 hover animation
        style={
            "transition": "all 0.3s ease",
        },

        _hover={
            "transform": "translateY(-6px) scale(1.02)",
            "border_color": "#84cc16",
            "box_shadow": "0 20px 40px rgba(132,204,22,0.2)"
        },
    )