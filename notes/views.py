from django.http import HttpRequest, HttpResponse
from django.middleware.csrf import get_token
from django.urls import reverse
from django.utils.html import escape

from notes import data


def html_shell(title: str, body: str) -> str:
    safe_title = escape(title)

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">

        <title>{safe_title}</title>

        <style>
            * {{
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }}

            html {{
                scroll-behavior: smooth;
            }}

            body {{
                font-family:
                    Inter,
                    -apple-system,
                    BlinkMacSystemFont,
                    "Segoe UI",
                    sans-serif;

                min-height: 100vh;

                color: #f8fafc;

                background:
                    radial-gradient(
                        circle at 10% 10%,
                        rgba(124, 58, 237, 0.25),
                        transparent 30%
                    ),
                    radial-gradient(
                        circle at 90% 20%,
                        rgba(6, 182, 212, 0.20),
                        transparent 30%
                    ),
                    linear-gradient(
                        135deg,
                        #09090f,
                        #11111b 45%,
                        #09090f
                    );

                overflow-x: hidden;
            }}

            body::before {{
                content: "";
                position: fixed;
                inset: 0;

                background:
                    linear-gradient(
                        rgba(255,255,255,0.015) 1px,
                        transparent 1px
                    ),
                    linear-gradient(
                        90deg,
                        rgba(255,255,255,0.015) 1px,
                        transparent 1px
                    );

                background-size: 40px 40px;
                pointer-events: none;
                z-index: -1;
            }}

            a {{
                color: inherit;
                text-decoration: none;
            }}

            .container {{
                width: min(1100px, calc(100% - 40px));
                margin: 0 auto;
                padding: 60px 0;
            }}

            .navbar {{
                position: sticky;
                top: 20px;

                z-index: 100;

                width: min(1100px, calc(100% - 40px));
                margin: 20px auto 0;

                display: flex;
                justify-content: space-between;
                align-items: center;

                padding: 16px 22px;

                background: rgba(17, 17, 27, 0.72);
                backdrop-filter: blur(18px);

                border: 1px solid rgba(255,255,255,0.08);
                border-radius: 18px;

                box-shadow:
                    0 20px 60px rgba(0,0,0,0.30),
                    inset 0 1px 0 rgba(255,255,255,0.04);
            }}

            .brand {{
                display: flex;
                align-items: center;
                gap: 12px;

                font-size: 17px;
                font-weight: 800;
                letter-spacing: -0.3px;
            }}

            .brand-icon {{
                width: 38px;
                height: 38px;

                display: flex;
                align-items: center;
                justify-content: center;

                border-radius: 12px;

                font-size: 18px;
                font-weight: 900;

                background:
                    linear-gradient(
                        135deg,
                        #7c3aed,
                        #06b6d4
                    );

                box-shadow:
                    0 8px 30px rgba(124,58,237,0.4);
            }}

            .nav-links {{
                display: flex;
                gap: 8px;
            }}

            .nav-link {{
                padding: 9px 14px;

                color: #a1a1aa;

                border-radius: 10px;

                transition:
                    background 0.2s ease,
                    color 0.2s ease,
                    transform 0.2s ease;
            }}

            .nav-link:hover {{
                color: white;
                background: rgba(255,255,255,0.06);
                transform: translateY(-1px);
            }}

            .hero {{
                text-align: center;
                padding: 80px 0 70px;
            }}

            .hero-badge {{
                display: inline-flex;
                align-items: center;
                gap: 8px;

                padding: 8px 14px;

                font-size: 13px;
                font-weight: 700;

                color: #d8b4fe;

                border: 1px solid rgba(168,85,247,0.25);
                border-radius: 999px;

                background: rgba(124,58,237,0.10);

                margin-bottom: 24px;
            }}

            .hero h1 {{
                max-width: 850px;
                margin: 0 auto;

                font-size: clamp(42px, 7vw, 76px);
                line-height: 0.98;
                letter-spacing: -4px;
                font-weight: 900;

                background:
                    linear-gradient(
                        135deg,
                        #ffffff 0%,
                        #ddd6fe 35%,
                        #67e8f9 100%
                    );

                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
            }}

            .hero p {{
                max-width: 650px;
                margin: 26px auto 0;

                color: #a1a1aa;

                font-size: 17px;
                line-height: 1.7;
            }}

            .hero-actions {{
                margin-top: 34px;

                display: flex;
                justify-content: center;
                gap: 12px;

                flex-wrap: wrap;
            }}

            .btn {{
                display: inline-flex;
                align-items: center;
                gap: 8px;

                padding: 13px 20px;

                border-radius: 12px;

                font-weight: 700;

                transition:
                    transform 0.2s ease,
                    box-shadow 0.2s ease,
                    background 0.2s ease;
            }}

            .btn-primary {{
                background:
                    linear-gradient(
                        135deg,
                        #7c3aed,
                        #4f46e5
                    );

                box-shadow:
                    0 12px 35px rgba(124,58,237,0.35);
            }}

            .btn-primary:hover {{
                transform: translateY(-3px);
                box-shadow:
                    0 18px 45px rgba(124,58,237,0.45);
            }}

            .btn-secondary {{
                background: rgba(255,255,255,0.05);
                border: 1px solid rgba(255,255,255,0.08);
            }}

            .btn-secondary:hover {{
                transform: translateY(-3px);
                background: rgba(255,255,255,0.08);
            }}

            .section-header {{
                margin-bottom: 25px;
            }}

            .section-title {{
                font-size: 30px;
                font-weight: 850;
                letter-spacing: -1px;
            }}

            .section-subtitle {{
                margin-top: 7px;
                color: #71717a;
            }}

            .notes-grid {{
                display: grid;
                grid-template-columns:
                    repeat(auto-fit, minmax(300px, 1fr));

                gap: 18px;
            }}

            .note-card {{
                position: relative;

                padding: 26px;

                background:
                    linear-gradient(
                        145deg,
                        rgba(255,255,255,0.075),
                        rgba(255,255,255,0.025)
                    );

                border: 1px solid rgba(255,255,255,0.08);
                border-radius: 22px;

                backdrop-filter: blur(14px);

                overflow: hidden;

                transition:
                    transform 0.25s ease,
                    border-color 0.25s ease,
                    box-shadow 0.25s ease;
            }}

            .note-card::before {{
                content: "";

                position: absolute;

                width: 160px;
                height: 160px;

                top: -90px;
                right: -80px;

                background: #7c3aed;

                border-radius: 50%;

                filter: blur(70px);
                opacity: 0.18;

                transition:
                    opacity 0.25s ease,
                    transform 0.25s ease;
            }}

            .note-card:hover {{
                transform: translateY(-7px);

                border-color:
                    rgba(167,139,250,0.35);

                box-shadow:
                    0 25px 60px rgba(0,0,0,0.35);
            }}

            .note-card:hover::before {{
                opacity: 0.35;
                transform: scale(1.4);
            }}

            .note-number {{
                color: #71717a;
                font-size: 12px;
                font-weight: 800;
                letter-spacing: 1px;
                text-transform: uppercase;
            }}

            .note-title {{
                margin-top: 12px;

                font-size: 22px;
                line-height: 1.2;
                font-weight: 800;
            }}

            .note-preview {{
                margin-top: 12px;

                color: #a1a1aa;

                line-height: 1.6;
                font-size: 14px;
            }}

            .meta {{
                display: flex;
                align-items: center;
                gap: 8px;

                margin-top: 20px;

                flex-wrap: wrap;
            }}

            .tag,
            .category {{
                padding: 7px 10px;

                font-size: 12px;
                font-weight: 700;

                border-radius: 999px;
            }}

            .tag {{
                color: #c4b5fd;

                background:
                    rgba(124,58,237,0.12);

                border:
                    1px solid rgba(124,58,237,0.20);
            }}

            .category {{
                color: #67e8f9;

                background:
                    rgba(6,182,212,0.10);

                border:
                    1px solid rgba(6,182,212,0.18);
            }}

            .read-more {{
                display: inline-flex;
                align-items: center;

                gap: 6px;

                margin-top: 20px;

                font-size: 13px;
                font-weight: 800;

                color: white;
            }}

            .read-more span {{
                transition: transform 0.2s ease;
            }}

            .note-card:hover .read-more span {{
                transform: translateX(4px);
            }}

            .article-wrapper {{
                max-width: 850px;
                margin: 70px auto;
            }}

            .article {{
                padding: 45px;

                background:
                    linear-gradient(
                        145deg,
                        rgba(255,255,255,0.075),
                        rgba(255,255,255,0.025)
                    );

                border: 1px solid rgba(255,255,255,0.08);
                border-radius: 28px;

                backdrop-filter: blur(18px);

                box-shadow:
                    0 30px 100px rgba(0,0,0,0.35);
            }}

            .article h1 {{
                font-size: clamp(36px, 6vw, 60px);
                line-height: 1.02;
                letter-spacing: -2.5px;
            }}

            .article-body {{
                margin-top: 30px;

                font-size: 17px;
                line-height: 1.9;

                color: #d4d4d8;
            }}

            .article-meta {{
                margin-top: 28px;

                display: flex;
                gap: 10px;

                flex-wrap: wrap;
            }}

            .back-link {{
                display: inline-flex;
                align-items: center;
                gap: 8px;

                margin-top: 32px;

                padding: 12px 16px;

                border-radius: 12px;

                background:
                    rgba(255,255,255,0.05);

                border:
                    1px solid rgba(255,255,255,0.08);

                color: #d4d4d8;

                transition:
                    transform 0.2s ease,
                    background 0.2s ease;
            }}

            .back-link:hover {{
                transform: translateX(-3px);
                background: rgba(255,255,255,0.08);
            }}
            
                        .form-wrapper {{
                max-width: 720px;
                margin: 70px auto;
            }}

            .form-card {{
                position: relative;
                padding: 42px;

                border: 1px solid rgba(255,255,255,0.08);
                border-radius: 28px;

                background:
                    linear-gradient(
                        145deg,
                        rgba(255,255,255,0.075),
                        rgba(255,255,255,0.025)
                    );

                backdrop-filter: blur(18px);

                box-shadow:
                    0 30px 100px rgba(0,0,0,0.35);

                overflow: hidden;
            }}

            .form-card::before {{
                content: "";
                position: absolute;

                width: 260px;
                height: 260px;

                top: -140px;
                right: -100px;

                border-radius: 50%;

                background: #7c3aed;
                filter: blur(100px);

                opacity: 0.15;
            }}

            .form-title {{
                position: relative;

                font-size: clamp(34px, 5vw, 52px);
                line-height: 1;
                letter-spacing: -2px;

                font-weight: 800;

                background:
                    linear-gradient(
                        135deg,
                        #ffffff,
                        #c4b5fd,
                        #67e8f9
                    );

                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
            }}

            .form-subtitle {{
                position: relative;

                margin-top: 12px;

                color: #71717a;
                font-size: 14px;
                line-height: 1.6;
            }}

            .form {{
                position: relative;

                margin-top: 32px;

                display: flex;
                flex-direction: column;
                gap: 20px;
            }}

            .form-group {{
                display: flex;
                flex-direction: column;
                gap: 8px;
            }}

            .form-label {{
                color: #d4d4d8;
                font-size: 13px;
                font-weight: 700;
            }}

            .form-input {{
                width: 100%;

                padding: 14px 15px;

                border: 1px solid rgba(255,255,255,0.08);
                border-radius: 12px;

                outline: none;

                background: rgba(255,255,255,0.04);
                color: #f8fafc;

                font-family: inherit;
                font-size: 14px;

                transition:
                    border-color 0.2s ease,
                    background 0.2s ease,
                    box-shadow 0.2s ease;
            }}

            .form-input::placeholder {{
                color: #52525b;
            }}

            .form-input:focus {{
                border-color: rgba(139,92,246,0.55);

                background: rgba(255,255,255,0.06);

                box-shadow:
                    0 0 0 4px rgba(139,92,246,0.10);
            }}

            .form-textarea {{
                min-height: 180px;
                resize: vertical;
            }}

            .form-actions {{
                display: flex;
                align-items: center;
                gap: 12px;

                margin-top: 4px;

                flex-wrap: wrap;
            }}

            .submit-button {{
                border: none;
                cursor: pointer;

                display: inline-flex;
                align-items: center;
                justify-content: center;

                padding: 14px 20px;

                border-radius: 12px;

                background:
                    linear-gradient(
                        135deg,
                        #7c3aed,
                        #4f46e5
                    );

                color: white;

                font-family: inherit;
                font-size: 14px;
                font-weight: 800;

                box-shadow:
                    0 12px 35px rgba(124,58,237,0.3);

                transition:
                    transform 0.2s ease,
                    box-shadow 0.2s ease;
            }}

            .submit-button:hover {{
                transform: translateY(-3px);

                box-shadow:
                    0 18px 45px rgba(124,58,237,0.42);
            }}

            .form-error {{
                margin-bottom: 20px;

                padding: 13px 15px;

                border: 1px solid rgba(239,68,68,0.2);
                border-radius: 12px;

                background: rgba(239,68,68,0.08);

                color: #fca5a5;

                font-size: 13px;
            }}

            .success-wrapper {{
                max-width: 700px;
                margin: 100px auto;
            }}

            .success-card {{
                padding: 45px;

                text-align: center;

                border: 1px solid rgba(34,197,94,0.15);
                border-radius: 28px;

                background:
                    linear-gradient(
                        145deg,
                        rgba(255,255,255,0.075),
                        rgba(255,255,255,0.025)
                    );

                backdrop-filter: blur(18px);

                box-shadow:
                    0 30px 100px rgba(0,0,0,0.35);
            }}

            .success-icon {{
                width: 64px;
                height: 64px;

                margin: 0 auto 22px;

                display: flex;
                align-items: center;
                justify-content: center;

                border-radius: 20px;

                background: rgba(34,197,94,0.10);

                border:
                    1px solid rgba(34,197,94,0.18);

                color: #86efac;

                font-size: 28px;
            }}

            .success-title {{
                font-size: 40px;
                letter-spacing: -1.5px;
                font-weight: 800;
            }}

            .success-text {{
                margin-top: 14px;

                color: #a1a1aa;

                font-size: 14px;
                line-height: 1.7;
            }}

            .success-details {{
                margin-top: 20px;

                padding: 15px;

                border-radius: 14px;

                background: rgba(255,255,255,0.04);

                color: #d4d4d8;

                font-size: 14px;
            }}

            .success-details strong {{
                color: white;
            }}

            @media (max-width: 700px) {{
                .form-wrapper {{
                    margin: 45px auto;
                }}

                .form-card {{
                    padding: 25px;
                    border-radius: 20px;
                }}

                .success-wrapper {{
                    margin: 60px auto;
                }}

                .success-card {{
                    padding: 28px 22px;
                    border-radius: 20px;
                }}

                .success-title {{
                    font-size: 32px;
                }}
            }}
            
            .footer {{
                padding: 30px 0 50px;

                text-align: center;

                color: #52525b;

                font-size: 13px;
            }}

            .footer strong {{
                color: #71717a;
            }}

            @media (max-width: 700px) {{
                .container {{
                    width: min(100% - 24px, 1100px);
                    padding: 35px 0;
                }}

                .navbar {{
                    width: calc(100% - 24px);
                }}

                .nav-links {{
                    display: none;
                }}

                .hero {{
                    padding: 55px 0 45px;
                }}

                .hero h1 {{
                    letter-spacing: -2.5px;
                }}

                .article {{
                    padding: 25px;
                    border-radius: 20px;
                }}

                .note-card {{
                    padding: 22px;
                }}
            }}
        </style>
    </head>

    <body>

        <nav class="navbar">
            <a href="{escape(reverse('index'))}" class="brand">
                <div class="brand-icon">N</div>
                <span>My Django Notes</span>
            </a>

            <div class="nav-links">
                <a class="nav-link" href="{escape(reverse('index'))}">
                    Home
                </a>

                <a class="nav-link" href="{escape(reverse('notes_list'))}">
                    Notes
                </a>

                <a class="nav-link" href="{escape(reverse('about'))}">
                    About
                </a>
            </div>
        </nav>

        {body}

        <footer class="footer">
            Built with <strong>Python + Django</strong> 🚀
        </footer>

    </body>
    </html>
    """


def _csrf_field(request: HttpRequest) -> str:
    token = get_token(request)
    return f"<input type='hidden' name='csrfmiddlewaretoken' value='{escape(token)}' />"


def index(request: HttpRequest) -> HttpResponse:
    body = f"""
    <main class="container">

        <section class="hero">

            <div class="hero-badge">
                <span>●</span>
                Django Developer Workspace
            </div>

            <h1>
                Welcome to<br>
                Django Notes
            </h1>

            <p>
                My personal space for programming notes,
                backend development, Python, Django and
                everything I learn along the way.
            </p>

            <div class="hero-actions">

                <a
                    class="btn btn-primary"
                    href="{escape(reverse('notes_list'))}"
                >
                    Explore Notes →
                </a>

                <a
                    class="btn btn-secondary"
                    href="{escape(reverse('about'))}"
                >
                    About Project
                </a>

            </div>

        </section>

    </main>
    """

    return HttpResponse(html_shell("index", body))


def about(request: HttpRequest) -> HttpResponse:
    body = f"""
    <main class="container">

        <section class="hero">

            <div class="hero-badge">
                About the project
            </div>

            <h1>
                Python.<br>
                Django.<br>
                Learning.
            </h1>

            <p>
                This is my first Django project.
                I'm using it to learn web development,
                backend architecture and Python.
            </p>

            <div class="hero-actions">

                <a
                    class="btn btn-primary"
                    href="{escape(reverse('notes_list'))}"
                >
                    View Notes →
                </a>

                <a
                    class="btn btn-secondary"
                    href="{escape(reverse('index'))}"
                >
                    ← Home
                </a>

            </div>

        </section>

    </main>
    """

    return HttpResponse(html_shell("About Django", body))


def notes_list(request: HttpRequest) -> HttpResponse:
    raw_tag = request.GET.get("tag")
    raw_category = request.GET.get("category")

    notes = data.list_notes()

    if raw_tag:
        tag_filter = raw_tag.strip().lower()
        notes = [n for n in notes if n['tag'].lower() == tag_filter]

    if raw_category:
        category_filter = raw_category.strip().lower()
        notes = [n for n in notes if n['category'].lower() == category_filter]

    items: list[str] = []

    for index, note in enumerate(notes, start=1):

        url = reverse(
            "note_detail",
            kwargs={"note_id": note["id"]}
        )

        items.append(
            f"""
            <a href="{escape(url)}" class="note-card">

                <div class="note-number">
                    Note #{index:02d}
                </div>

                <div class="note-title">
                    {escape(note["title"])}
                </div>

                <div class="note-preview">
                    {escape(note["body"][:120])}...
                </div>

                <div class="meta">

                    <span class="category">
                        {escape(note["category"])}
                    </span>

                    <span class="tag">
                        #{escape(note["tag"])}
                    </span>

                </div>

                <div class="read-more">
                    Read note
                    <span>→</span>
                </div>

            </a>
            """
        )

    body = f"""
    <main class="container">

        <section class="hero" style="padding-bottom: 45px;">

            <div class="hero-badge">
                Knowledge Base
            </div>

            <h1>
                My Notes
            </h1>

            <p>
                Thoughts, tutorials, experiments and
                useful things I've learned while coding.
            </p>

        </section>

        <section>

            <div class="section-header">

                <div class="section-title">
                    All Notes
                </div>

                <div class="section-subtitle">
                    {len(notes)} notes available
                </div>

            </div>

            <div class="notes-grid">
                {"".join(items)}
            </div>

        </section>

    </main>
    """

    return HttpResponse(html_shell("Notes List", body))


def note_detail(request: HttpRequest, note_id: int) -> HttpResponse:
    note = data.get_note(note_id)

    edit_url = escape(
        reverse(
            "note_edit",
            kwargs={"note_id": note_id}
        )
    )

    delete_url = escape(
        reverse(
            "note_delete",
            kwargs={"note_id": note_id}
        )
    )

    body = f"""
    <main class="container">

        <div class="article-wrapper">

            <article class="article">

                <div class="hero-badge">
                    Note #{note_id}
                </div>

                <h1>
                    {escape(note["title"])}
                </h1>

                <div class="article-meta">

                    <span class="category">
                        {escape(note["category"])}
                    </span>

                    <span class="tag">
                        #{escape(note["tag"])}
                    </span>

                </div>

                <div class="article-body">
                    {escape(note["body"])}
                </div>

                <div class="hero-actions">

                    <a
                        href="{edit_url}"
                        class="btn btn-primary"
                    >
                        Edit Note
                    </a>

                    <a
                        href="{delete_url}"
                        class="btn btn-secondary"
                    >
                        Delete Note
                    </a>

                    <a
                        href="{escape(reverse("notes_list"))}"
                        class="btn btn-secondary"
                    >
                        ← Return to notes
                    </a>

                </div>

            </article>

        </div>

    </main>
    """

    return HttpResponse(
        html_shell(
            f"{note['title']}",
            body
        )
    )


def note_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        title = request.POST["title"]
        category = request.POST["category"]
        tag = request.POST["tag"]
        body = request.POST["body"]

        if not title.strip():
            err = "<p>Title can not be empty</p>"
        else:
            created = data.create_note(
                title=title,
                category=category,
                tag=tag or 'different',
                body=body or 'main'
            )
            list_url = escape(reverse("notes_list"))
            return HttpResponse(
                html_shell(
                    "Note Created",
                    f"""
                    <main class="success-wrapper">

                        <section class="success-card">

                            <div class="success-icon">
                                ✓
                            </div>

                            <h1 class="success-title">
                                Note Created
                            </h1>

                            <p class="success-text">
                                Your note has been successfully added.
                            </p>

                            <div class="success-details">
                                id =
                                <strong>{created['id']}</strong>
                                ,
                                title =
                                <strong>
                                    {escape(created['title'])}
                                </strong>
                            </div>

                            <div class="hero-buttons">
                                <a
                                    class="button button-primary"
                                    href="{list_url}"
                                >
                                    Return to Notes →
                                </a>
                            </div>

                        </section>

                    </main>
                    """
                )
            )
    else:
        err = "<p>Method Not Allowed</p>"

    action = f"{escape(reverse('note_create'))}"

    form = f"""
    <main class="form-wrapper">

        <section class="form-card">

            <div class="hero-badge">
                Create something new
            </div>

            <h1 class="form-title">
                New Note
            </h1>

            <p class="form-subtitle">
                Add a new note to your Django knowledge base.
            </p>

            {f'<div class="form-error">{err}</div>' if err else ''}

            <form method="POST" action="{action}" class="form">

                {_csrf_field(request)}

                <div class="form-group">
                    <label class="form-label">
                        Title
                    </label>

                    <input
                        class="form-input"
                        type="text"
                        name="title"
                        placeholder="Enter note title..."
                        required
                    >
                </div>

                <div class="form-group">
                    <label class="form-label">
                        Note
                    </label>

                    <textarea
                        class="form-input form-textarea"
                        name="body"
                        placeholder="Write your note..."
                        required
                    ></textarea>
                </div>

                <div class="form-group">
                    <label class="form-label">
                        Category
                    </label>

                    <input
                        class="form-input"
                        type="text"
                        name="category"
                        placeholder="Python, Django, SQL..."
                        required
                    >
                </div>

                <div class="form-group">
                    <label class="form-label">
                        Tag
                    </label>

                    <input
                        class="form-input"
                        type="text"
                        name="tag"
                        placeholder="backend, python..."
                        required
                    >
                </div>

                <div class="form-actions">

                    <button
                        type="submit"
                        class="submit-button"
                    >
                        Create Note →
                    </button>

                    <a
                        href="{escape(reverse('notes_list'))}"
                        class="button button-secondary"
                    >
                        Cancel
                    </a>

                </div>

            </form>

        </section>

    </main>
    """

    return HttpResponse(html_shell("Note Create", form))


def note_edit(request: HttpRequest, note_id: int) -> HttpResponse:
    note = data.get_note(note_id)

    if request.method == "POST":
        title = request.POST["title"]
        category = request.POST["category"]
        tag = request.POST["tag"]
        body = request.POST["body"]

        if not title.strip():
            err = "<p>Title can not be empty</p>"
        else:
            updated = data.update_note(
                note_id=note_id,
                title=title,
                category=category,
                tag=tag or "different",
                body=body or "main",
            )

            detail_url = escape(
                reverse(
                    "note_detail",
                    kwargs={"note_id": note_id},
                )
            )

            return HttpResponse(
                html_shell(
                    "Note Updated",
                    f"""
                    <main class="success-wrapper">

                        <section class="success-card">

                            <div class="success-icon">
                                ✓
                            </div>

                            <div class="hero-badge">
                                Note updated
                            </div>

                            <h1 class="success-title">
                                Note Updated
                            </h1>

                            <p class="success-text">
                                id = {updated['id']},
                                title = {escape(updated['title'])}
                            </p>

                            <div class="hero-buttons">

                                <a
                                    href="{detail_url}"
                                    class="button button-primary"
                                >
                                    Return to note →
                                </a>

                            </div>

                        </section>

                    </main>
                    """
                )
            )
    else:
        err = ""

    action = escape(
        reverse(
            "note_edit",
            kwargs={"note_id": note_id},
        )
    )

    form = f"""
        <main class="form-wrapper">

            <section class="form-card">

                <div class="hero-badge">
                    Edit your note
                </div>

                <h1 class="form-title">
                    Edit Note
                </h1>

                <p class="form-subtitle">
                    Update the information of your note.
                </p>

                {f'<div class="form-error">{err}</div>' if err else ''}

                <form
                    method="POST"
                    action="{action}"
                    class="form"
                >

                    {_csrf_field(request)}

                    <div class="form-group">
                        <label class="form-label">
                            Title
                        </label>

                        <input
                            class="form-input"
                            type="text"
                            name="title"
                            value="{escape(note['title'])}"
                            required
                        >
                    </div>

                    <div class="form-group">
                        <label class="form-label">
                            Note
                        </label>

                        <textarea
                            class="form-input form-textarea"
                            name="body"
                            required
                        >{escape(note['body'])}</textarea>
                    </div>

                    <div class="form-group">
                        <label class="form-label">
                            Category
                        </label>

                        <input
                            class="form-input"
                            type="text"
                            name="category"
                            value="{escape(note['category'])}"
                            required
                        >
                    </div>

                    <div class="form-group">
                        <label class="form-label">
                            Tag
                        </label>

                        <input
                            class="form-input"
                            type="text"
                            name="tag"
                            value="{escape(note['tag'])}"
                            required
                        >
                    </div>

                    <div class="form-actions">

                        <button
                            type="submit"
                            class="submit-button"
                        >
                            Save Changes →
                        </button>

                        <a
                            href="{escape(
                                reverse(
                                    'note_detail',
                                    kwargs={'note_id': note_id}
                                )
                            )}"
                            class="button button-secondary"
                        >
                            Cancel
                        </a>

                    </div>

                </form>

            </section>

        </main>
    """

    return HttpResponse(
        html_shell("Note Edit", form)
    )


def note_delete(request: HttpRequest, note_id: int) -> HttpResponse:
    note = data.get_note(note_id)

    if request.method == "POST":
        data.delete_note(note_id)

        list_url = escape(
            reverse("notes_list")
        )

        return HttpResponse(
            html_shell(
                "Note Deleted",
                f"""
                <main class="success-wrapper">

                    <section class="success-card">

                        <div class="success-icon">
                            ✓
                        </div>

                        <div class="hero-badge">
                            Deletion completed
                        </div>

                        <h1 class="success-title">
                            Note Deleted
                        </h1>

                        <p class="success-text">
                            Note
                            <strong>
                                {escape(note['title'])}
                            </strong>
                            was deleted successfully.
                        </p>

                        <div class="hero-buttons">

                            <a
                                href="{list_url}"
                                class="button button-primary"
                            >
                                Return to notes →
                            </a>

                        </div>

                    </section>

                </main>
                """
            )
        )

    action = escape(
        reverse(
            "note_delete",
            kwargs={"note_id": note_id},
        )
    )

    list_url = escape(
        reverse("notes_list")
    )

    detail_url = escape(
        reverse(
            "note_detail",
            kwargs={"note_id": note_id},
        )
    )

    form = f"""
        <main class="success-wrapper">

            <section class="success-card">

                <div class="hero-badge">
                    Delete note
                </div>

                <h1 class="success-title">
                    Delete Note?
                </h1>

                <p class="success-text">
                    Are you sure you want to delete
                    <strong>
                        "{escape(note['title'])}"
                    </strong>
                    ?
                </p>

                <form
                    method="POST"
                    action="{action}"
                    class="hero-buttons"
                >

                    {_csrf_field(request)}

                    <button
                        type="submit"
                        class="submit-button"
                    >
                        Delete Note
                    </button>

                    <a
                        href="{detail_url}"
                        class="button button-secondary"
                    >
                        Cancel
                    </a>

                </form>

            </section>

        </main>
    """

    return HttpResponse(
        html_shell("Note Delete", form)
    )