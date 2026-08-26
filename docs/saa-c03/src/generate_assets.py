"""Generate cover, exam-domain, and diagram-convention images for the study guide."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ASSETS = Path(__file__).resolve().parent.parent / "assets"
NAVY = (35, 47, 62, 255)
ORANGE = (255, 153, 0, 255)
WHITE = (255, 255, 255, 255)
TEAL = (27, 107, 147, 255)
SLATE = (84, 91, 100, 255)
LIGHT = (244, 247, 249, 255)
BODY = (43, 43, 43, 255)
GREEN = (30, 142, 62, 255)
AMBER = (196, 133, 0, 255)
RED = (209, 50, 18, 255)
BOX_FILL = (255, 255, 255, 255)
VPC_FILL = (232, 238, 242, 255)
PUBLIC = (255, 246, 232, 255)
PRIVATE = (231, 246, 236, 255)
SG = (253, 236, 236, 255)


def _font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def fonts():
    regular = "/usr/share/fonts/truetype/macos/Inter-Regular.ttf"
    medium = "/usr/share/fonts/truetype/macos/Inter-Medium.ttf"
    semibold = "/usr/share/fonts/truetype/macos/Inter-SemiBold.ttf"
    bold = "/usr/share/fonts/truetype/macos/Inter-Bold.ttf"
    return {
        "regular": lambda s: _font(regular, s),
        "medium": lambda s: _font(medium, s),
        "semibold": lambda s: _font(semibold, s),
        "bold": lambda s: _font(bold, s),
    }


def rounded_rect(draw: ImageDraw.ImageDraw, box, radius, fill, outline=None, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def center_text(draw, xy, text, font, fill):
    x, y = xy
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text((x - w / 2, y - h / 2), text, font=font, fill=fill)


def wrapped_center(draw, box, text, font, fill):
    x0, y0, x1, y1 = box
    max_w = x1 - x0 - 16
    words = text.split()
    lines = []
    current = ""
    for word in words:
        trial = (current + " " + word).strip()
        bbox = draw.textbbox((0, 0), trial, font=font)
        if bbox[2] - bbox[0] <= max_w:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    line_h = draw.textbbox((0, 0), "Ag", font=font)[3] - draw.textbbox((0, 0), "Ag", font=font)[1] + 4
    total = line_h * len(lines)
    y = (y0 + y1) / 2 - total / 2
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        w = bbox[2] - bbox[0]
        draw.text(((x0 + x1) / 2 - w / 2, y), line, font=font, fill=fill)
        y += line_h


def generate_cover_banner(path: Path) -> None:
    f = fonts()
    img = Image.new("RGBA", (2400, 620), NAVY)
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 590, 2400, 620), fill=ORANGE)
    draw.rectangle((0, 0, 28, 620), fill=ORANGE)
    draw.text((80, 70), "PERSONAL PRACTICAL-LAB JOURNAL", font=f["semibold"](28), fill=ORANGE)
    draw.text((80, 130), "AWS Certified Solutions Architect", font=f["bold"](64), fill=WHITE)
    draw.text((80, 215), "Associate (SAA-C03)", font=f["bold"](64), fill=WHITE)
    draw.text(
        (80, 320),
        "Practical Experiments and Study Guide",
        font=f["medium"](38),
        fill=(210, 218, 226, 255),
    )
    draw.rectangle((80, 385, 420, 389), fill=ORANGE)
    draw.text((80, 420), "Learner: Kritheebhan", font=f["medium"](28), fill=WHITE)
    draw.text((80, 470), "Version 0.1  ·  Foundation edition  ·  26 August 2026", font=f["regular"](24), fill=(176, 186, 196, 255))
    draw.text((80, 520), "Status: Awaiting Experiment 1 notes and screenshots", font=f["semibold"](24), fill=ORANGE)
    img.convert("RGB").save(path, "PNG", dpi=(300, 300))


def generate_domain_chart(path: Path) -> None:
    f = fonts()
    img = Image.new("RGBA", (1800, 980), WHITE)
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 1800, 980), fill=LIGHT)
    draw.rounded_rectangle((40, 30, 1760, 950), radius=18, fill=WHITE, outline=(197, 205, 211, 255), width=2)
    draw.text((80, 60), "SAA-C03 scored content by domain", font=f["bold"](36), fill=NAVY)
    draw.text(
        (80, 115),
        "Weights published in the official AWS exam guide. Confirm the live exam code before you book.",
        font=f["regular"](20),
        fill=SLATE,
    )

    domains = [
        ("Domain 1", "Design Secure Architectures", 30, ORANGE),
        ("Domain 2", "Design Resilient Architectures", 26, TEAL),
        ("Domain 3", "Design High-Performing Architectures", 24, NAVY),
        ("Domain 4", "Design Cost-Optimized Architectures", 20, GREEN),
    ]
    origin_x, origin_y = 430, 200
    max_bar = 1180
    bar_h = 92
    gap = 38
    for i, (code, name, weight, color) in enumerate(domains):
        y = origin_y + i * (bar_h + gap)
        draw.text((80, y + 18), code, font=f["bold"](22), fill=NAVY)
        draw.text((80, y + 50), name, font=f["regular"](18), fill=SLATE)
        track = (origin_x, y + 18, origin_x + max_bar, y + 18 + 56)
        rounded_rect(draw, track, 10, (232, 238, 242, 255))
        bar_w = int(max_bar * (weight / 30.0))
        rounded_rect(draw, (origin_x, y + 18, origin_x + bar_w, y + 74), 10, color)
        label = f"{weight}%"
        draw.text((origin_x + bar_w + 18, y + 28), label, font=f["bold"](26), fill=NAVY)

    draw.text(
        (80, 860),
        "Security carries the largest share of scored questions. Cost still matters, but it has the smallest weight.",
        font=f["regular"](20),
        fill=SLATE,
    )
    img.convert("RGB").save(path, "PNG", dpi=(220, 220))


def generate_architecture_legend(path: Path) -> None:
    f = fonts()
    img = Image.new("RGBA", (2000, 1280), WHITE)
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 2000, 1280), fill=LIGHT)
    draw.rounded_rectangle((30, 24, 1970, 1256), radius=18, fill=WHITE, outline=(197, 205, 211, 255), width=2)
    draw.text((70, 50), "Architecture diagram conventions", font=f["bold"](34), fill=NAVY)
    draw.text(
        (70, 100),
        "This is a layout key only. It is not an experiment architecture and does not describe a deployed lab.",
        font=f["regular"](20),
        fill=SLATE,
    )

    # Users
    user_box = (90, 180, 320, 300)
    rounded_rect(draw, user_box, 14, BOX_FILL, TEAL, 3)
    wrapped_center(draw, user_box, "Users / clients", f["semibold"](22), NAVY)

    # Internet
    inet = (430, 180, 680, 300)
    rounded_rect(draw, inet, 14, PUBLIC, ORANGE, 3)
    wrapped_center(draw, inet, "Internet / public edge", f["semibold"](22), NAVY)

    # Arrow user -> internet
    draw.line((320, 240, 430, 240), fill=NAVY, width=4)
    draw.polygon([(430, 240), (412, 230), (412, 250)], fill=NAVY)

    # VPC boundary
    vpc = (90, 360, 1910, 1040)
    rounded_rect(draw, vpc, 18, VPC_FILL, NAVY, 4)
    draw.text((120, 380), "VPC boundary  ·  network isolation", font=f["bold"](22), fill=NAVY)

    # Public subnet
    pub = (130, 450, 760, 780)
    rounded_rect(draw, pub, 14, PUBLIC, ORANGE, 3)
    draw.text((160, 470), "Public subnet", font=f["bold"](22), fill=NAVY)
    alb = (180, 530, 430, 640)
    rounded_rect(draw, alb, 12, BOX_FILL, TEAL, 3)
    wrapped_center(draw, alb, "Load balancer or public service", f["medium"](18), BODY)
    nat = (470, 530, 720, 640)
    rounded_rect(draw, nat, 12, BOX_FILL, TEAL, 3)
    wrapped_center(draw, nat, "NAT / internet path", f["medium"](18), BODY)
    sg1 = (180, 670, 720, 750)
    rounded_rect(draw, sg1, 10, SG, RED, 3)
    wrapped_center(draw, sg1, "Security group  ·  allow listed ports only", f["medium"](18), BODY)

    # Private subnet
    priv = (820, 450, 1860, 980)
    rounded_rect(draw, priv, 14, PRIVATE, GREEN, 3)
    draw.text((850, 470), "Private subnet", font=f["bold"](22), fill=NAVY)
    app = (870, 530, 1280, 680)
    rounded_rect(draw, app, 12, BOX_FILL, TEAL, 3)
    wrapped_center(draw, app, "Application compute (EC2, ECS, Lambda in VPC)", f["medium"](18), BODY)
    data = (1340, 530, 1820, 680)
    rounded_rect(draw, data, 12, BOX_FILL, TEAL, 3)
    wrapped_center(draw, data, "Data store (RDS, DynamoDB via endpoint, EFS)", f["medium"](18), BODY)
    iam = (870, 720, 1280, 840)
    rounded_rect(draw, iam, 12, BOX_FILL, NAVY, 3)
    wrapped_center(draw, iam, "IAM role  ·  least privilege", f["medium"](18), BODY)
    kms = (1340, 720, 1820, 840)
    rounded_rect(draw, kms, 12, BOX_FILL, NAVY, 3)
    wrapped_center(draw, kms, "Encryption / KMS  ·  at rest", f["medium"](18), BODY)
    logs = (870, 870, 1820, 950)
    rounded_rect(draw, logs, 12, BOX_FILL, SLATE, 3)
    wrapped_center(draw, logs, "Logging and monitoring  ·  CloudWatch / CloudTrail", f["medium"](18), BODY)

    # arrows inside
    draw.line((760, 585, 820, 585), fill=NAVY, width=4)
    draw.polygon([(820, 585), (802, 575), (802, 595)], fill=NAVY)
    draw.line((1280, 605, 1340, 605), fill=NAVY, width=4)
    draw.polygon([(1340, 605), (1322, 595), (1322, 615)], fill=NAVY)

    # Internet to VPC
    draw.line((555, 300, 555, 450), fill=NAVY, width=4)
    draw.polygon([(555, 450), (545, 432), (565, 432)], fill=NAVY)

    draw.text(
        (90, 1080),
        "Every experiment diagram will show users, AWS services, request flow, network boundaries, and security controls.",
        font=f["regular"](20),
        fill=SLATE,
    )
    draw.text(
        (90, 1130),
        "Sensitive values such as account IDs, emails, access keys, and IP addresses must be hidden before a screenshot is inserted.",
        font=f["regular"](20),
        fill=SLATE,
    )
    img.convert("RGB").save(path, "PNG", dpi=(220, 220))


def generate_process_chart(path: Path) -> None:
    f = fonts()
    img = Image.new("RGBA", (2000, 720), WHITE)
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 2000, 720), fill=LIGHT)
    draw.rounded_rectangle((30, 24, 1970, 696), radius=18, fill=WHITE, outline=(197, 205, 211, 255), width=2)
    draw.text((70, 50), "How each experiment is added to this document", font=f["bold"](32), fill=NAVY)

    steps = [
        ("1", "You send notes\nand screenshots"),
        ("2", "Missing items\nare listed"),
        ("3", "Chapter is drafted\nin original wording"),
        ("4", "You confirm\ntechnical values"),
        ("5", "Approved chapter\nis added and indexed"),
    ]
    x = 80
    y = 180
    w, h = 320, 280
    for i, (num, label) in enumerate(steps):
        box = (x, y, x + w, y + h)
        rounded_rect(draw, box, 16, WHITE, TEAL if i < 4 else ORANGE, 4)
        circle = (x + w / 2 - 36, y + 36, x + w / 2 + 36, y + 108)
        draw.ellipse(circle, fill=ORANGE if i == 0 else NAVY)
        center_text(draw, (x + w / 2, y + 72), num, f["bold"](32), WHITE)
        wrapped_center(draw, (x + 20, y + 130, x + w - 20, y + h - 20), label.replace("\n", " "), f["semibold"](22), NAVY)
        if i < len(steps) - 1:
            draw.line((x + w + 8, y + h / 2, x + w + 48, y + h / 2), fill=NAVY, width=4)
            draw.polygon(
                [(x + w + 56, y + h / 2), (x + w + 38, y + h / 2 - 12), (x + w + 38, y + h / 2 + 12)],
                fill=NAVY,
            )
        x += w + 64
    draw.text(
        (70, 520),
        "No experiment chapter is written until lab notes or screenshots are supplied. Uncertain values are marked [Verification required].",
        font=f["regular"](20),
        fill=SLATE,
    )
    draw.text(
        (70, 570),
        "After every five completed experiments, a revision checkpoint and progress summary are added.",
        font=f["regular"](20),
        fill=SLATE,
    )
    img.convert("RGB").save(path, "PNG", dpi=(220, 220))


def generate_all() -> dict[str, Path]:
    ASSETS.mkdir(parents=True, exist_ok=True)
    paths = {
        "cover": ASSETS / "cover-banner.png",
        "domains": ASSETS / "saa-c03-domain-weights.png",
        "legend": ASSETS / "architecture-diagram-conventions.png",
        "process": ASSETS / "experiment-update-process.png",
    }
    generate_cover_banner(paths["cover"])
    generate_domain_chart(paths["domains"])
    generate_architecture_legend(paths["legend"])
    generate_process_chart(paths["process"])
    return paths


if __name__ == "__main__":
    generate_all()
    print("Assets written to", ASSETS)
