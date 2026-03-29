import reflex as rx
from RAG_PROJECT.components.navbar import navbar
from RAG_PROJECT.states.rag_state import ChatState


def history():
    return rx.vstack(
        navbar(),

        rx.vstack(

            # 🔥 HEADER (AI STYLE)
            rx.vstack(
                rx.text(
                    "AI MEMORY",
                    color="#84cc16",
                    font_size="11px",
                    font_weight="700",
                    letter_spacing="0.2em",
                ),
                rx.heading(
                    "Conversation History",
                    size="8",
                    color="#ecfccb",
                    font_weight="800",
                ),
                rx.text(
                    "All your past AI interactions are stored and are accessible instantly.",
                    color="#a3a3a3",
                    font_size="14px",
                ),
                spacing="2",
                margin_bottom="25px",
                align="start",
            ),

            # CONTENT
            rx.cond(
                ChatState.history.length() == 0,

                # EMPTY STATE
                rx.box(
                    rx.vstack(
                        rx.icon(tag="clock", size=50, color="#84cc16"),
                        rx.text(
                            "No conversations yet",
                            color="#d9f99d",
                            font_weight="600",
                        ),
                        rx.text(
                            "Start chatting to build your AI memory ⚡",
                            color="#737373",
                        ),
                        align="center",
                        spacing="3",
                        padding="60px",
                    ),
                    border="1px dashed #84cc1640",
                    border_radius="16px",
                    width="100%",
                    background="#0a0f1a",
                ),

                # HISTORY LIST
                rx.vstack(
                    rx.foreach(
                        ChatState.history,
                        lambda item: history_card(item)
                    ),

                    # ACTION BUTTONS
                    rx.hstack(
                        rx.button(
                            rx.icon(tag="trash-2", size=16),
                            "Clear History",
                            on_click=ChatState.clear_history,
                            background="#1f2937",
                            color="#f87171",
                            border="1px solid #ef4444",
                            _hover={
                                "background": "#ef4444",
                                "color": "white",
                                "transform": "scale(1.05)"
                            },
                            transition="all 0.2s",
                        ),

                        rx.button(
                            rx.icon(tag="download", size=16),
                            "Download PDF",
                            on_click=ChatState.download_chat,
                            background="#84cc16",
                            color="#020617",
                            font_weight="600",
                            _hover={
                                "background": "#65a30d",
                                "transform": "scale(1.05)"
                            },
                            transition="all 0.2s",
                            box_shadow="0 0 20px #84cc1650",
                        ),

                        spacing="4",
                        margin_top="25px",
                        justify="end",
                        width="100%",
                    ),

                    spacing="4",
                    width="100%",
                )
            ),

            width="100%",
            max_width="850px",
            margin="0 auto",
            padding="40px",
            background="#020617",
            border_radius="20px",
            border="1px solid #1f2937",
            box_shadow="0 0 40px rgba(132,204,22,0.08)",
            margin_top="40px",
        ),

        width="100%",
        min_height="100vh",
        background="radial-gradient(circle at top, #020617, #000000)",
        padding_bottom="60px",
    )


def history_card(item):
    return rx.box(
        rx.vstack(

            # QUESTION
            rx.hstack(
                rx.icon(tag="user", size=16, color="#84cc16"),
                rx.text(
                    item.question,
                    font_weight="700",
                    color="#ecfccb",
                    size="3"
                ),
                align="center",
                spacing="2",
            ),

            # ANSWER
            rx.box(
                rx.text(
                    item.answer,
                    color="#d4d4d4",
                    font_size="14px",
                    line_height="1.7",
                ),
                padding="16px",
                background="#020617",
                border_radius="12px",
                border="1px solid #84cc1620",
                width="100%",
            ),

            # SOURCES
            rx.cond(
                item.sources != "",
                rx.hstack(
                    rx.badge(
                        item.sources,
                        background="#84cc1620",
                        color="#84cc16",
                        border_radius="full",
                    ),
                    margin_top="6px",
                )
            ),

            spacing="3",
            align="start",
            width="100%",
        ),

        padding="20px",
        background="#020617",
        border="1px solid #1f2937",
        border_radius="16px",
        width="100%",

        # 🔥 ANIMATIONS
        style={
            "transition": "all 0.25s ease",
            "animation": "fadeIn 0.4s ease",
            "_hover": {
                "border_color": "#84cc16",
                "box_shadow": "0 0 25px #84cc1630",
                "transform": "translateY(-3px) scale(1.01)",
            },
        },
    )