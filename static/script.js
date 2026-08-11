const searchInput = document.getElementById("searchInput");

if (searchInput) {
    searchInput.addEventListener("keyup", function () {

        let value = searchInput.value.toLowerCase();
        let cards = document.querySelectorAll(".card");

        cards.forEach(function (card) {

            let text = card.innerText.toLowerCase();

            if (text.includes(value)) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }

        });

    });
}


// Mobile Menu
function toggleMenu() {
    let menu = document.getElementById("navLinks");

    if (menu) {
        menu.classList.toggle("active");
    }
}


// Dark / Light Theme
function toggleTheme() {

    document.body.classList.toggle("light-mode");

    let btn = document.getElementById("themeBtn");

    if (btn) {
        if (document.body.classList.contains("light-mode")) {
            btn.innerHTML = "☀️";
        } else {
            btn.innerHTML = "🌙";
        }
    }
}


// Filter AI Tools
function filterTools(category) {

    const cards = document.querySelectorAll(".card");

    cards.forEach(function (card) {

        if (category === "all") {
            card.style.display = "block";
        }

        else if (card.classList.contains(category)) {
            card.style.display = "block";
        }

        else {
            card.style.display = "none";
        }

    });
}
/* ================= AI TOOL FINDER ================= */

function findAITool() {

    const input = document.getElementById("finderInput");
    const result = document.getElementById("finderResult");

    if (!input || !result) {
        return;
    }

    const query = input.value.toLowerCase().trim();

    if (query === "") {

        result.innerHTML = `
            <div class="finder-result-icon">💬</div>
            <h3>Tell me what you need!</h3>
            <p>
                Example: "I need an AI for coding"
            </p>
        `;

        return;
    }

    let tool = null;

    /* Coding */

    if (
        query.includes("coding") ||
        query.includes("code") ||
        query.includes("programming") ||
        query.includes("developer")
    ) {

        tool = {
            icon: "💻",
            name: "GitHub Copilot",
            description: "An AI coding assistant that helps developers write and understand code.",
            link: "https://github.com/features/copilot"
        };

    }

    /* Images / Design */

    else if (
        query.includes("image") ||
        query.includes("picture") ||
        query.includes("design") ||
        query.includes("graphic")
    ) {

        tool = {
            icon: "🎨",
            name: "Canva AI",
            description: "Create graphics, designs and visual content with AI.",
            link: "https://www.canva.com"
        };

    }

    /* Video / YouTube */

    else if (
        query.includes("video") ||
        query.includes("youtube") ||
        query.includes("reel") ||
        query.includes("movie")
    ) {

        tool = {
            icon: "🎬",
            name: "Runway ML",
            description: "Create and edit AI-powered videos and visual content.",
            link: "https://runwayml.com"
        };

    }

    /* Music */

    else if (
        query.includes("music") ||
        query.includes("song") ||
        query.includes("audio")
    ) {

        tool = {
            icon: "🎵",
            name: "Suno AI",
            description: "Create songs and music using artificial intelligence.",
            link: "https://suno.com"
        };

    }

    /* Writing */

    else if (
        query.includes("writing") ||
        query.includes("write") ||
        query.includes("essay") ||
        query.includes("article") ||
        query.includes("content")
    ) {

        tool = {
            icon: "✍️",
            name: "ChatGPT",
            description: "A powerful AI assistant for writing, ideas, learning and content creation.",
            link: "https://chatgpt.com"
        };

    }

    /* Research */

    else if (
        query.includes("research") ||
        query.includes("search") ||
        query.includes("information") ||
        query.includes("study")
    ) {

        tool = {
            icon: "🔎",
            name: "Perplexity AI",
            description: "An AI-powered search and research assistant.",
            link: "https://www.perplexity.ai"
        };

    }

    /* General AI */

    else {

        tool = {
            icon: "🤖",
            name: "ChatGPT",
            description: "A versatile AI assistant for writing, coding, learning, brainstorming and much more.",
            link: "https://chatgpt.com"
        };

    }

    result.innerHTML = `
        <div class="finder-result-icon">${tool.icon}</div>

        <h3>✨ We found a great match!</h3>

        <div class="finder-tool">

            <strong>
                ${tool.icon} ${tool.name}
            </strong>

            <p>
                ${tool.description}
            </p>

            <a href="${tool.link}" target="_blank" rel="noopener noreferrer">
                🚀 Try ${tool.name}
            </a>

        </div>
    `;

}