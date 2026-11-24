import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a crisp mobile + desktop preview mockup image of the updated landing page & audit launcher
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 6.2), gridspec_kw={'width_ratios': [1.05, 1.35]})
fig.patch.set_facecolor('#070d19')

# --- Left Panel: Mobile View (390px style) ---
ax1.set_facecolor('#070d19')
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 100)
ax1.axis('off')

# Phone frame
phone = patches.FancyBboxPatch((12, 4), 76, 92, boxstyle="round,pad=1.5,rounding_size=6",
                               facecolor='#0b1120', edgecolor='#38bdf8', linewidth=2)
ax1.add_patch(phone)
ax1.text(50, 92.5, "MOBILE VIEW (390px)", color='#38bdf8', fontsize=9, fontweight='bold', ha='center')

# Header bar inside phone
ax1.add_patch(patches.FancyBboxPatch((16, 82), 68, 7, boxstyle="round,pad=0.5,rounding_size=2",
                                     facecolor='#0f172a', edgecolor='#334155', linewidth=1))
# Logo square + P
ax1.add_patch(patches.FancyBboxPatch((18.5, 83.2), 4.6, 4.6, boxstyle="round,pad=0.2,rounding_size=1.2",
                                     facecolor='#162033', edgecolor='#34d399', linewidth=1.2))
ax1.text(20.8, 85.5, "P", color='#f8fafc', fontsize=8.5, fontweight='bold', ha='center', va='center')
ax1.text(25.5, 85.8, "Paul Adikemere O.", color='#f8fafc', fontsize=7.5, fontweight='bold', va='center')
ax1.text(79, 85.5, "☰", color='#38bdf8', fontsize=10, ha='center', va='center')

# Hero badge & headline
ax1.add_patch(patches.FancyBboxPatch((23, 74), 54, 4.5, boxstyle="round,pad=0.3,rounding_size=2",
                                     facecolor='#102438', edgecolor='#38bdf8', linewidth=0.8))
ax1.text(50, 76.2, "● AEO & GEO Visibility Consultant", color='#38bdf8', fontsize=6.5, fontweight='bold', ha='center', va='center')

ax1.text(50, 68.5, "Get Recommended by\nChatGPT, Perplexity,\nGemini & Grok", color='#f8fafc',
         fontsize=9.5, fontweight='bold', ha='center', va='center', linespacing=1.25)

ax1.text(50, 58.5, "Structured copy, Q&A & schema\nwith zero visual redesign.", color='#94a3b8',
         fontsize=6.8, ha='center', va='center', linespacing=1.25)

# Stacked mobile CTA buttons (full-width touch targets)
ax1.add_patch(patches.FancyBboxPatch((18, 48.5), 64, 5.5, boxstyle="round,pad=0.3,rounding_size=1.8",
                                     facecolor='#38bdf8', edgecolor='none'))
ax1.text(50, 51.25, "Request Your 1-Page Sample", color='#06101d', fontsize=7.5, fontweight='bold', ha='center', va='center')

ax1.add_patch(patches.FancyBboxPatch((18, 41.5), 64, 5.5, boxstyle="round,pad=0.3,rounding_size=1.8",
                                     facecolor='#0f172a', edgecolor='#475569', linewidth=1))
ax1.text(50, 44.25, "Open AI Audit Launcher →", color='#f8fafc', fontsize=7.5, fontweight='bold', ha='center', va='center')

# Mobile scorecard preview
ax1.add_patch(patches.FancyBboxPatch((18, 9), 64, 29.5, boxstyle="round,pad=0.4,rounding_size=2.5",
                                     facecolor='#0f172a', edgecolor='#38bdf8', linewidth=1.2))
ax1.text(50, 35.5, "4 AI ENGINES SCORECARD", color='#38bdf8', fontsize=6.8, fontweight='bold', ha='center')

engines = [("ChatGPT", "Skipped", "Cited #1"),
           ("Perplexity", "Skipped", "Cited #1"),
           ("Gemini", "Partial", "Cited #1"),
           ("Grok", "Skipped", "Cited #1")]
for idx, (name, before, after) in enumerate(engines):
    y_pos = 29.5 - idx * 5.6
    ax1.add_patch(patches.FancyBboxPatch((20.5, y_pos - 1.6), 59, 4.0, boxstyle="round,pad=0.2,rounding_size=1",
                                         facecolor='#070d19', edgecolor='#1e293b', linewidth=0.8))
    ax1.text(22.5, y_pos + 0.4, name, color='#f8fafc', fontsize=6.5, fontweight='bold', va='center')
    ax1.text(53, y_pos + 0.4, before, color='#f87171', fontsize=5.8, fontweight='bold', ha='center', va='center')
    ax1.text(71, y_pos + 0.4, after, color='#34d399', fontsize=5.8, fontweight='bold', ha='center', va='center')

# --- Right Panel: Desktop View ---
ax2.set_facecolor('#070d19')
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 100)
ax2.axis('off')

desktop = patches.FancyBboxPatch((4, 10), 92, 86, boxstyle="round,pad=1.2,rounding_size=4",
                                 facecolor='#0b1120', edgecolor='#34d399', linewidth=2)
ax2.add_patch(desktop)
ax2.text(50, 92.5, "DESKTOP VIEW — LIVE HERO & SCORECARD", color='#34d399', fontsize=9, fontweight='bold', ha='center')

# Top nav bar
ax2.add_patch(patches.FancyBboxPatch((7, 81), 86, 7.5, boxstyle="round,pad=0.4,rounding_size=2",
                                     facecolor='#0f172a', edgecolor='#334155', linewidth=1))
ax2.add_patch(patches.FancyBboxPatch((9.5, 82.3), 4.8, 4.8, boxstyle="round,pad=0.2,rounding_size=1.2",
                                     facecolor='#162033', edgecolor='#38bdf8', linewidth=1.2))
ax2.text(11.9, 84.7, "P", color='#f8fafc', fontsize=8.5, fontweight='bold', ha='center', va='center')
ax2.text(16.2, 84.7, "Paul Adikemere O.", color='#f8fafc', fontsize=7.8, fontweight='bold', va='center')
ax2.text(89, 84.7, "How It Works   Audit ($200)   FAQ   Launcher", color='#94a3b8', fontsize=6.3, fontweight='bold', ha='right', va='center')

# Left column inside desktop hero
ax2.add_patch(patches.FancyBboxPatch((8, 69.5), 34, 4.5, boxstyle="round,pad=0.3,rounding_size=2",
                                     facecolor='#102438', edgecolor='#38bdf8', linewidth=0.8))
ax2.text(25, 71.75, "● AEO & GEO Visibility Consultant", color='#38bdf8', fontsize=6.4, fontweight='bold', ha='center', va='center')

ax2.text(8, 57, "Get Recommended by\nChatGPT, Perplexity,\nGemini & Grok", color='#f8fafc',
         fontsize=10.5, fontweight='bold', ha='left', va='center', linespacing=1.25)

ax2.text(8, 42, "High-intent buyers ask AI who to hire.\nI structure your copy, Q&A & schema\nwith zero visual redesign.", color='#94a3b8',
         fontsize=6.8, ha='left', va='center', linespacing=1.3)

ax2.add_patch(patches.FancyBboxPatch((8, 27.5), 22, 6, boxstyle="round,pad=0.3,rounding_size=1.6",
                                     facecolor='#38bdf8', edgecolor='none'))
ax2.text(19, 30.5, "Request 1-Page Sample", color='#06101d', fontsize=6.8, fontweight='bold', ha='center', va='center')

ax2.add_patch(patches.FancyBboxPatch((32, 27.5), 18, 6, boxstyle="round,pad=0.3,rounding_size=1.6",
                                     facecolor='#0f172a', edgecolor='#475569', linewidth=1))
ax2.text(41, 30.5, "AI Audit Launcher →", color='#f8fafc', fontsize=6.8, fontweight='bold', ha='center', va='center')

# Right column inside desktop hero: Scorecard card
ax2.add_patch(patches.FancyBboxPatch((53, 25), 39, 50.5, boxstyle="round,pad=0.4,rounding_size=2.5",
                                     facecolor='#0f172a', edgecolor='#38bdf8', linewidth=1.2))
ax2.text(72.5, 72, "LIVE BUYER PROMPT SIMULATION", color='#94a3b8', fontsize=6.3, fontweight='bold', ha='center')

for idx, (name, before, after) in enumerate(engines):
    y_pos = 64 - idx * 10.5
    ax2.add_patch(patches.FancyBboxPatch((55.5, y_pos - 3.2), 34, 6.8, boxstyle="round,pad=0.25,rounding_size=1.5",
                                         facecolor='#070d19', edgecolor='#1e293b', linewidth=0.9))
    ax2.text(57.5, y_pos + 0.2, name, color='#f8fafc', fontsize=7.2, fontweight='bold', va='center')
    ax2.text(75.5, y_pos + 0.2, before, color='#f87171', fontsize=6.2, fontweight='bold', ha='center', va='center')
    ax2.text(85.5, y_pos + 0.2, after, color='#34d399', fontsize=6.2, fontweight='bold', ha='center', va='center')

# Bottom audit offer strip in desktop preview
ax2.add_patch(patches.FancyBboxPatch((8, 13.5), 84, 8, boxstyle="round,pad=0.3,rounding_size=2",
                                     facecolor='#162033', edgecolor='#34d399', linewidth=1.1))
ax2.text(11, 17.5, "Full Multi-Prompt Audit & Blueprint (48-Hr Turnaround)", color='#f8fafc', fontsize=7.2, fontweight='bold', va='center')
ax2.text(89, 17.5, "$200  •  100% Credited to Implementation", color='#34d399', fontsize=7.2, fontweight='bold', ha='right', va='center')

plt.tight_layout(pad=1.2)
plt.savefig("site_preview.png", dpi=180, facecolor='#070d19')
print("Saved site_preview.png")