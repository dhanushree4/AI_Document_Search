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


# 🔹 CARD STYLE (smooth lift using Reflex)
def card_style():
    return {
        "transition": "all 0.3s ease",
        "_hover": {
            "transform": "translateY(-6px)",
            "border": f"1px solid {ACCENT}",
            "box_shadow": f"0 0 15px {ACCENT}",
        },
    }


# 🔹 HOVER TEXT (✨ highlight on hover)
def hover_text(content):
    return rx.text(
        content,
        color=SUBTEXT,
        font_size="13px",
        style={
            "transition": "all 0.25s ease",
            "_hover": {
                "color": ACCENT,
                "transform": "translateX(4px)",
            },
        },
    )


# 🔹 TECH BADGE
def tech_badge(label: str):
    return rx.box(
        rx.text(label, color=TEXT, font_size="12px"),
        padding_x="12px",
        padding_y="5px",
        bg=CARD,
        border=f"1px solid {BORDER}",
        border_radius="6px",
        style={
            "transition": "all 0.2s ease",
            "_hover": {
                "background": "#111827",
                "transform": "scale(1.05)",
                "border": f"1px solid {ACCENT}",
            },
        },
    )


# 🔹 ARCHITECTURE STEP (with hover animation)
def arch_step(num: str, title: str, desc: str):
    return rx.hstack(
        rx.box(
            rx.text(num, color=BG, font_size="11px", font_weight="700"),
            bg=ACCENT,
            width="26px",
            height="26px",
            border_radius="50%",
            display="flex",
            align_items="center",
            justify_content="center",
        ),
        rx.vstack(
            rx.text(
                title,
                color=TEXT,
                font_size="14px",
                font_weight="600",
                style={
                    "transition": "0.25s",
                    "_hover": {"color": ACCENT},
                },
            ),
            hover_text(desc),
            align="start",
        ),
        spacing="4",
        align="start",
        width="100%",
    )


# 🔹 FEATURE CARD
def feature_card(icon: str, title: str, desc: str):
    return rx.box(
        rx.vstack(
            rx.icon(icon, size=24, color=ACCENT),
            rx.text(title, color=TEXT, font_size="14px", font_weight="600"),
            rx.text(desc, color=SUBTEXT, font_size="12px", text_align="center"),
            spacing="2",
            align="center",
        ),
        padding="20px",
        bg=CARD,
        border=f"1px solid {BORDER}",
        border_radius="12px",
        style={
            "transition": "all 0.3s ease",
            "cursor": "pointer",
            "_hover": {
                "transform": "translateY(-8px)",
                "border": f"1px solid {ACCENT}",
                "box_shadow": f"0 10px 25px -5px rgba(132, 204, 22, 0.2)",
            },
        },
    )


def about():
    return rx.box(
        navbar(),

        rx.box(
            rx.vstack(

                # 🌿 HERO
                rx.vstack(
                    rx.text(
                        "ABOUT THE SYSTEM",
                        color=ACCENT,
                        font_size="11px",
                        font_weight="600",
                        letter_spacing="0.15em",
                    ),
                    rx.heading(
                        "DataTalk",
                        size="8",
                        color=TEXT,
                        font_weight="700",
                        style={
                            "transition": "0.3s",
                            "_hover": {"color": ACCENT},
                        },
                    ),
                    rx.text(
                        "DataTalk is an intelligent document analysis system built using "
                        "Retrieval-Augmented Generation (RAG). It enables users to interact "
                        "with documents through natural language while ensuring context-aware "
                        "and accurate responses.",
                        color=SUBTEXT,
                        font_size="15px",
                        max_width="750px",
                        line_height="1.7",
                    ),
                    spacing="3",
                    align="start",
                    margin_bottom="40px",
                ),

                # 🌿 GRID - 2 COLUMN LAYOUT
                rx.grid(

                    # 🔹 LEFT: ARCHITECTURE (DETAILED)
                    rx.box(
                        rx.vstack(
                            rx.text("SYSTEM ARCHITECTURE", color=ACCENT, font_size="11px", font_weight="600"),

                            arch_step(
                                "1",
                                "Document Ingestion",
                                "Supports PDF and text files using PyPDFLoader and TextLoader for structured data extraction."
                            ),
                            arch_step(
                                "2",
                                "Preprocessing Pipeline",
                                "Cleans and normalizes text while preserving semantic structure for downstream processing."
                            ),
                            arch_step(
                                "3",
                                "Chunking Strategy",
                                "Uses RecursiveCharacterTextSplitter (chunk size 300, overlap 30) for optimal context retention."
                            ),
                            arch_step(
                                "4",
                                "Embedding Generation",
                                "Generates dense vector embeddings using all-MiniLM-L6-v2 (384-dimensional semantic vectors)."
                            ),
                            arch_step(
                                "5",
                                "Vector Database",
                                "Stores embeddings in ChromaDB with efficient similarity-based indexing."
                            ),
                            arch_step(
                                "6",
                                "Semantic Retrieval",
                                "Uses Max Marginal Relevance (MMR) to retrieve diverse and relevant document chunks."
                            ),
                            arch_step(
                                "7",
                                "Context Optimization",
                                "Refines queries and ensures high-quality contextual input before response generation."
                            ),
                            arch_step(
                                "8",
                                "Answer Generation",
                                "Generates responses using LLaMA 3.1 (via Groq) with context-aware prompting."
                            ),

                            spacing="3",
                        ),
                        padding="28px",
                        bg=CARD,
                        border=f"1px solid {BORDER}",
                        border_radius="16px",
                        style=card_style(),
                    ),

                    # 🔹 RIGHT: TECH STACK + RAG + KEY FEATURES
                    rx.vstack(

                        # TECH STACK
                        rx.box(
                            rx.vstack(
                                rx.text("TECH STACK", color=ACCENT, font_size="11px"),
                                rx.flex(
                                    tech_badge("Python"),
                                    tech_badge("Reflex"),
                                    tech_badge("LangChain"),
                                    tech_badge("Groq"),
                                    tech_badge("ChromaDB"),
                                    tech_badge("Transformers"),
                                    wrap="wrap",
                                    gap="2",
                                ),
                            ),
                            padding="22px",
                            bg=CARD,
                            border=f"1px solid {BORDER}",
                            border_radius="16px",
                            style=card_style(),
                        ),

                        # RAG EXPLANATION
                        rx.box(
                            rx.vstack(
                                rx.text("RETRIEVAL-AUGMENTED GENERATION", color=ACCENT, font_size="11px"),
                                rx.text(
                                    "RAG enhances traditional language models by grounding responses "
                                    "in external knowledge sources. Instead of relying solely on model memory, "
                                    "it retrieves relevant document context and combines it with generation, "
                                    "resulting in more accurate and reliable outputs.",
                                    color=SUBTEXT,
                                    font_size="14px",
                                    line_height="1.7",
                                ),
                            ),
                            padding="22px",
                            bg=CARD,
                            border=f"1px solid {BORDER}",
                            border_radius="16px",
                            style=card_style(),
                        ),

                        # KEY FEATURES
                        rx.box(
                            rx.vstack(
                                rx.text("KEY FEATURES", color=ACCENT, font_size="11px"),
                                rx.grid(
                                    feature_card("upload", "Multi-Format", "PDF and TXT support"),
                                    feature_card("search", "Semantic Search", "Context-aware retrieval"),
                                    feature_card("shield", "Data Privacy", "Local processing only"),
                                    feature_card("zap", "Fast Response", "Low-latency queries"),
                                    columns="2",
                                    gap="3",
                                    width="100%",
                                ),
                            ),
                            padding="22px",
                            bg=CARD,
                            border=f"1px solid {BORDER}",
                            border_radius="16px",
                            style=card_style(),
                        ),

                        spacing="5",
                    ),

                    columns="2",
                    spacing="6",
                    width="100%",
                ),

                max_width="1400px",
                margin="0 auto",
                padding="48px 40px",
            ),
        ),

        footer(),

        bg=f"linear-gradient(135deg, {BG}, #111827, {BG})",
        min_height="100vh",
    )