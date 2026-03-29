import reflex as rx

from RAG_PROJECT.components.navbar import navbar
from RAG_PROJECT.states.rag_state import ChatState


def chat() -> rx.Component:
    return rx.box(
        navbar(),

        rx.box(
            rx.vstack(

                # ─── HEADER (NEW) ─────────────────────────
                rx.hstack(
                    rx.hstack(
                        rx.icon(tag="bot", size=22, color="#a3b18a"),
                        rx.heading(
                            "AI Assistant",
                            size="5",
                            color="#e2e8f0",
                            font_weight="700"
                        ),
                        spacing="3",
                        align="center",
                    ),

                    rx.spacer(),

                    rx.text(
                        "Powered by RAG",
                        color="#64748b",
                        font_size="12px"
                    ),

                    width="100%",
                    padding="16px 20px",
                    border_bottom="1px solid #1e293b",
                    background="rgba(2,6,23,0.7)",
                    backdrop_filter="blur(10px)",
                ),

                # ─── CHAT AREA ───────────────────────────
                rx.box(
                    rx.vstack(

                        # EMPTY STATE
                        rx.cond(
                            ChatState.history.length() == 0,
                            rx.vstack(
                                rx.icon(tag="bot", size=50, color="#334155"),
                                rx.text(
                                    "Start chatting with your documents",
                                    color="#64748b",
                                    font_size="18px",
                                    font_weight="500",
                                ),
                                spacing="3",
                                align="center",
                                justify="center",
                                height="100%",
                                width="100%",
                                 ), # full width for horizontal centering
                        ),

                        # MESSAGES
                        rx.foreach(
                            ChatState.history,
                            lambda item: message_pair(item)
                        ),

                        # LOADING
                        rx.cond(
                            ChatState.is_loading,
                            rx.hstack(
                                rx.spinner(size="2", color="#a3b18a"),
                                rx.text("Thinking...", color="#94a3b8"),
                                padding="12px",
                                border_radius="10px",
                                background="#020617",
                                border="1px solid #1e293b",
                            )
                        ),

                        spacing="5",
                        width="100%",
                    ),

                    width="100%",
                    flex="1",
                    overflow_y="auto",
                    padding="25px",

                    # ✨ SCROLL ANIMATION FEEL
                    style={
                        "scroll_behavior": "smooth"
                    }
                ),

                # ─── INPUT AREA ──────────────────────────
                rx.form(
                    rx.box(
                        rx.hstack(
                            rx.input(
                                name="chat_input",
                                placeholder="Ask anything about your documents...",
                                width="100%",
                                height="48px",
                                background="#020617",
                                color="#e2e8f0",
                                border="1px solid #1e293b",
                                border_radius="12px",
                                padding="0 15px",

                                # ✨ FOCUS GLOW
                                _focus={
                                    "border_color": "#a3b18a",
                                    "box_shadow": "0 0 0 2px rgba(163,177,138,0.25)"
                                }
                            ),

                            rx.button(
                                rx.icon(tag="send", size=18),
                                type="submit",
                                background="linear-gradient(135deg, #a3b18a, #588157)",
                                color="#020617",
                                border_radius="10px",
                                padding="12px",

                                # ✨ HOVER ANIMATION
                                _hover={
                                    "transform": "scale(1.08)",
                                    "box_shadow": "0 6px 20px rgba(163,177,138,0.3)"
                                },
                                transition="all 0.2s ease"
                            ),

                            spacing="3",
                            width="100%",
                        ),

                        padding="15px",
                        border_top="1px solid #1e293b",
                        background="#020617",
                    ),

                    on_submit=ChatState.handle_submit,
                    reset_on_submit=True,
                    width="100%",
                ),

                width="100%",
                max_width="900px",
                height="88vh",
                background="linear-gradient(180deg, #020617, #0f172a)",
                border_radius="14px",
                display="flex",
                flex_direction="column",
                overflow="hidden",

                # ✨ CARD DEPTH
                box_shadow="0 20px 60px rgba(0,0,0,0.5)",
            ),

            width="100%",
            display="flex",
            justify_content="center",
            padding="20px",
            min_height="100vh",

            # ✨ BACKGROUND GRADIENT
            background="radial-gradient(circle at top, #0f172a, #020617)",
        ),
    )


# ─────────────────────────────────────────────
# 💬 MESSAGE COMPONENT (ENHANCED)
# ─────────────────────────────────────────────

def message_pair(item):
    return rx.vstack(

        # USER MESSAGE
        rx.hstack(
            rx.spacer(),
            rx.box(
                rx.text(item.question, color="#020617"),

                background="linear-gradient(135deg, #a3b18a, #588157)",
                padding="12px 16px",
                border_radius="16px 16px 4px 16px",
                max_width="65%",

                # ✨ HOVER + ENTRY
                style={
                    "transition": "all 0.2s",
                },
                _hover={
                    "transform": "scale(1.02)"
                }
            ),
            width="100%",
        ),

        # AI MESSAGE
        rx.hstack(
            rx.box(
                rx.icon(tag="bot", size=18, color="#a3b18a"),
                padding="8px",
                background="#020617",
                border_radius="50%",
                border="1px solid #1e293b",
            ),

            rx.vstack(
                rx.box(
                    rx.text(
                        item.answer,
                        white_space="pre-wrap",
                        color="#e2e8f0",
                        line_height="1.7"
                    ),

                    background="#020617",
                    padding="16px",
                    border_radius="6px 16px 16px 16px",
                    border="1px solid #1e293b",

                    # ✨ HOVER EFFECT
                    _hover={
                        "border_color": "#a3b18a",
                        "transform": "translateY(-2px)"
                    },
                    transition="all 0.2s ease"
                ),

                rx.cond(
                    item.sources != "",
                    rx.text(
                        f"Source: {item.sources}",
                        font_size="11px",
                        color="#64748b",
                    )
                ),

                align="start",
                max_width="80%",
            ),

            spacing="3",
            width="100%",
        ),

        spacing="4",
        width="100%",
    )