import reflex as rx
import os

from RAG_PROJECT.components.navbar import navbar
from RAG_PROJECT.components.footer import footer
from RAG_PROJECT.backend.rag import build_vectorstore

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.join(BASE_DIR, "documents")
os.makedirs(UPLOAD_DIR, exist_ok=True)


class UploadState(rx.State):
    files: list[str] = []
    is_uploading: bool = False
    show_success_dialog: bool = False

    def close_dialog(self):
        self.show_success_dialog = False

    def load_files(self):
        if os.path.exists(UPLOAD_DIR):
            self.files = os.listdir(UPLOAD_DIR)

    def delete_file(self, filename: str):
        file_path = os.path.join(UPLOAD_DIR, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            self.load_files()
            build_vectorstore()

    async def handle_upload(self, files: list[rx.UploadFile]):
        if not files:
            return

        self.is_uploading = True
        yield
        
        for file in files:
            save_path = os.path.join(UPLOAD_DIR, file.filename)
            content = await file.read()
            with open(save_path, "wb") as f:
                f.write(content)
        
        self.load_files()
        build_vectorstore()
        
        self.is_uploading = False
        self.show_success_dialog = True
        yield rx.clear_selected_files("upload1")


def upload():
    return rx.box(
        navbar(),

        rx.box(
            rx.vstack(

                # ─── HEADER ─────────────────────────────
                rx.vstack(
                    rx.heading(
                        "Knowledge Base",
                        size="9",
                        color="#e2e8f0",
                        font_weight="800",
                    ),
                    rx.text(
                        "Upload documents and transform them into an intelligent, searchable AI system.",
                        color="#94a3b8",
                        font_size="15px",
                    ),
                    spacing="2",
                    align="center",
                    margin_bottom="40px",
                ),

                # ─── UPLOAD CARD ────────────────────────
                rx.box(
                    rx.upload(
                        rx.vstack(
                            rx.icon(tag="upload-cloud", size=50, color="#a3b18a"),
                            rx.text(
                                "Drag & drop files",
                                font_weight="600",
                                font_size="18px",
                                color="#e2e8f0",
                            ),
                            rx.text(
                                "or click to browse",
                                color="#64748b",
                                font_size="13px",
                            ),
                            spacing="3",
                            align="center",
                            padding="40px",
                        ),
                        id="upload1",
                        border="2px dashed #2f3e2f",
                        border_radius="18px",
                        background="#0f172a",
                        width="100%",
                        style={
                            "_hover": {
                                "border_color": "#a3b18a",
                                "background": "#111827",
                                "transform": "scale(1.01)"
                            },
                            "transition": "all 0.25s ease"
                        },
                    ),

                    # FILE QUEUE
                    rx.cond(
                        rx.selected_files("upload1"),
                        rx.vstack(
                            rx.text(
                                "Queued Files",
                                color="#a3b18a",
                                font_weight="600",
                                margin_top="20px"
                            ),
                            rx.foreach(
                                rx.selected_files("upload1"),
                                lambda f: rx.box(
                                    rx.hstack(
                                        rx.icon(tag="file-text", color="#a3b18a"),
                                        rx.text(f, color="#e2e8f0"),
                                    ),
                                    padding="10px 14px",
                                    border_radius="10px",
                                    background="#020617",
                                    border="1px solid #1e293b",
                                    style={
                                        "animation": "fadeIn 0.3s ease"
                                    }
                                )
                            ),
                            width="100%"
                        ),
                        rx.box()
                    ),

                    # BUTTON / LOADER
                    rx.cond(
                        UploadState.is_uploading,
                        rx.hstack(
                            rx.spinner(size="3"),
                            rx.text("Processing...", color="#a3b18a"),
                            align="center",
                            justify="center",
                            width="100%",
                            padding="12px",
                            background="#020617",
                            border_radius="10px",
                            margin_top="20px"
                        ),
                        rx.button(
                            "Upload Documents",
                            rx.icon(tag="upload", size=16),
                            on_click=UploadState.handle_upload(
                                rx.upload_files(upload_id="upload1")
                            ),
                            width="100%",
                            margin_top="20px",
                            size="4",
                            border_radius="10px",
                            background="#a3b18a",
                            color="#020617",
                            font_weight="600",
                            disabled=rx.selected_files("upload1").length() == 0,
                            style={
                                "_hover": {
                                    "transform": "translateY(-2px)",
                                    "box_shadow": "0 8px 25px rgba(163,177,138,0.3)"
                                },
                                "transition": "all 0.2s"
                            }
                        )
                    ),

                    width="100%",
                    max_width="650px",
                    padding="35px",
                    border_radius="20px",
                    background="rgba(15,23,42,0.6)",
                    backdrop_filter="blur(12px)",
                    border="1px solid rgba(255,255,255,0.05)",
                    box_shadow="0 10px 40px rgba(0,0,0,0.3)",
                ),

                # ─── FILE LIST ─────────────────────────
                rx.box(
                    rx.heading("Stored Documents", color="#e2e8f0", size="5"),

                    rx.cond(
                        UploadState.files.length() > 0,
                        rx.vstack(
                            rx.foreach(
                                UploadState.files,
                                lambda file: rx.hstack(
                                    rx.hstack(
                                        rx.icon(tag="check-circle", color="#a3b18a"),
                                        rx.text(file, color="#e2e8f0"),
                                        spacing="3",
                                    ),
                                    rx.spacer(),
                                    rx.button(
                                        rx.icon(tag="trash-2"),
                                        on_click=UploadState.delete_file(file),
                                        size="2",
                                        background="#7f1d1d",
                                        color="white",
                                        border_radius="8px",
                                        style={
                                            "_hover": {
                                                "background": "#991b1b",
                                                "transform": "scale(1.05)"
                                            }
                                        }
                                    ),
                                    padding="14px",
                                    border_radius="12px",
                                    background="#020617",
                                    border="1px solid #1e293b",
                                    width="100%",
                                    style={
                                        "_hover": {
                                            "transform": "translateY(-2px)",
                                            "border_color": "#a3b18a"
                                        },
                                        "transition": "all 0.2s"
                                    }
                                )
                            ),
                            spacing="3",
                            width="100%",
                        ),
                        rx.box(
                            rx.text(
                                "No documents uploaded yet.",
                                color="#64748b",
                                text_align="center",
                                padding="30px"
                            ),
                            border="1px dashed #1e293b",
                            border_radius="12px",
                            width="100%"
                        )
                    ),

                    width="100%",
                    max_width="650px",
                    margin_top="40px"
                ),

                spacing="6",
                align="center",
                width="100%",
                max_width="1100px",
                margin="0 auto",
                padding="40px"
            ),

            width="100%",
            min_height="100vh",
            background="linear-gradient(135deg, #020617, #0f172a, #020617)",
        ),

        # ─── SUCCESS MODAL ─────────────────────────
        rx.cond(
            UploadState.show_success_dialog,
            rx.box(
                rx.vstack(
                    rx.icon(tag="check-circle", size=50, color="#a3b18a"),
                    rx.heading("Upload Complete", color="#e2e8f0"),
                    rx.text(
                        "Your documents are now ready for intelligent querying.",
                        color="#94a3b8",
                        text_align="center"
                    ),
                    rx.hstack(
                        rx.button(
                            "Stay Here",
                            on_click=UploadState.close_dialog,
                            variant="outline"
                        ),
                        rx.button(
                            "Go to Chat",
                            on_click=rx.redirect("/chat"),
                            background="#a3b18a",
                            color="#020617"
                        ),
                        spacing="4",
                        margin_top="20px"
                    ),
                    align="center",
                    padding="40px",
                    border_radius="20px",
                    background="#020617",
                    border="1px solid #1e293b",
                ),
                position="fixed",
                top="0",
                left="0",
                width="100vw",
                height="100vh",
                background="rgba(0,0,0,0.7)",
                display="flex",
                align_items="center",
                justify_content="center",
                z_index="100"
            )
        ),

        footer(),
    )