import matplotlib.pyplot as plt

def create_chart(tools, percentages, title, filename):
    plt.figure()
    plt.bar(tools, percentages)
    plt.title(title)
    plt.xlabel("AI Tools")
    plt.ylabel("Percentage")
    plt.savefig(f"website/{filename}")
    plt.close()

# Content
create_chart(
    ["ChatGPT", "Gemini", "Copilot", "Claude"],
    [73.8, 11.9, 9.5, 2.4],
    "AI Tool Preference for Content Creation",
    "content_chart.png"
)

# Proofreading
create_chart(
    ["Grammarly", "ChatGPT", "Copilot", "Claude"],
    [54.8, 38.1, 4.8, 2.4],
    "AI Tool Preference for Proofreading",
    "proofreading_chart.png"
)

# Image
create_chart(
    ["Gemini", "Midjourney", "Copilot", "ChatGPT"],
    [40.5, 26.2, 9.5, 2.4],
    "AI Tool Preference for Image Generation",
    "image_chart.png"
)

# Info
create_chart(
    ["ChatGPT", "Copilot", "Gemini", "Search AI"],
    [66.7, 11.9, 9.5, 11.9],
    "AI Tool Preference for Information Seeking",
    "info_chart.png"
)