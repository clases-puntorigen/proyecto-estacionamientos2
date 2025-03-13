from nicegui_router import ThemeBuild

class TemaJose(ThemeBuild):
    def __init__(self) -> None:
        super().__init__(
            theme = {
                'primary': '#000000',     # Dark Charcoal for Main Background
                'secondary': '#F5F5F5',   # Light Gray for Drawer Background or Secondary elements
                'accent': '#FF6347',      # Lighter Orange-Red for subtle highlights
                'dark': '#333333',        # Lighter Charcoal for Sidebar and dark elements
                'positive': '#21ba45',    # Default Green for Positive states
                'negative': '#c10015',    # Default Red for Errors or Negative states
                'info': '#31ccec',        # Default Blue for Info states (optional to change)
                'warning': '#f2c037'      # Default Yellow for Warnings
            },
            font = "Poppins"
        )
