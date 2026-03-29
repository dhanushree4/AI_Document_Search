import reflex as rx

def navbar():
    return rx.box(
        rx.hstack(
            # ── LOGO ─────────────────────────────
            rx.hstack(
                rx.box(
                    rx.text(
                        "⬡",
                        font_size="22px",
                        color="#84cc16",  # lime green
                    ),
                    margin_right="6px",
                ),

                rx.text(
                    "Data",
                    font_size="20px",
                    font_weight="800",
                    color="#f1f5f9",
                    letter_spacing="0.10em",
                ),

                rx.text(
                    "Talk",
                    font_size="20px",
                    font_weight="800",
                    color="#84cc16",
                    letter_spacing="0.10em",
                ),

                align="center",
                spacing="0",
                style={
                    "transition": "all 0.3s ease",
                },
                _hover={
                    "transform": "scale(1.05)",
                },
            ),

            rx.spacer(),

            # ── NAV LINKS ───────────────────────
            rx.hstack(

                nav_link("Home", "/"),
                nav_link("Upload", "/upload"),
                nav_link("Chat", "/chat"),
                nav_link("History", "/history"),
                nav_link("About", "/about"),

                spacing="8",
                align="center",
            ),

            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding_x="32px",
            padding_y="16px",
            align="center",
        ),

        # ── NAVBAR STYLE ──────────────────────
        width="100%",
        position="sticky",
        top="0",
        z_index="100",

        # subtle glass + gradient
        background="rgba(8, 10, 15, 0.75)",
        backdrop_filter="blur(14px)",

        border_bottom="1px solid rgba(132,204,22,0.15)",

        # soft glow at bottom
        box_shadow="0 4px 30px rgba(132,204,22,0.05)",
    )


# ── REUSABLE NAV LINK COMPONENT ─────────────
def nav_link(label: str, href: str):
    return rx.link(
        rx.box(
            rx.text(
                label,
                font_size="13px",
                font_weight="600",
                letter_spacing="0.08em",
                text_transform="uppercase",
            ),

            # underline animation
            rx.box(
                height="2px",
                width="0%",
                background="#84cc16",
                position="absolute",
                bottom="-4px",
                left="0",
                transition="width 0.25s ease",
                class_name="nav-underline",
            ),

            position="relative",
            color="#94a3b8",

            style={
                "transition": "all 0.25s ease",
            },

            _hover={
                "color": "#84cc16",
                "transform": "translateY(-1px)",
            },
        ),
        href=href,
    )