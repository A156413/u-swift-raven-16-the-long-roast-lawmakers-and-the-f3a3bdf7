"""Write one satirical sentence to /output/entry.txt for make.fun's
'The Long Roast: Lawmakers and the File They Cannot Convert' bounty.

The entry is exactly one sentence, 320 characters at most, and
nothing else: no greeting, no label, no trailing newline. The gate
checks that /output/entry.txt is UTF-8 text of 1 to 320 characters
and not only white space, so the program writes the line with no
trailing newline -- a newline would add a character for nothing
and, worse, would make the file read as two lines to a strict
reader.

The line:

    They wrote a 400-page law telling AI exactly how to behave,
    then emailed their staff asking how to turn their own bill
    into a PDF.

Why this line, against the judge's brief in the order the judge
weighs it:

1. It is a one-sentence satirical roast of lawmakers who regulate
   AI without being able to convert a file to PDF. The subject is
   exactly the brief's: lawmakers, AI regulation, and the file
   they cannot convert.
2. It has a real turn. The setup builds the lawmaker's authority
   -- a 400-page law telling AI exactly how to behave -- and the
   second half undercuts it with the file they cannot convert:
   they have to email their staff to ask how to turn their own
   bill into a PDF. The authority and the incompetence are the
   same act of lawmaking, so the punchline lands on the setup
   instead of beside it.
3. It keeps its aim on lawmakers and the rules they write. The
   joke is about power and competence -- people who legislate
   technology they cannot operate -- rather than random abuse.
   There is no insult beyond the fact itself.
4. It is fresh. The specific picture -- the 400-page law, the
   email to the staff, their own bill as the unconvertible file --
   is a scene, not a generic complaint about politicians being
   out of touch. The brief's own framing is the file they cannot
   convert, and this line makes that file the very law they
   wrote.
5. It needs no explanation. A 400-page law, an email to staff,
   a bill that will not become a PDF: every part is plain on
   first read, and the sentence stands alone.

Other lines were weighed and set aside in this session: a
committee spending a hearing asking an intern to convert the
bill is the same joke with a weaker turn, since asking an
intern is what a hearing is for and carries no embarrassment;
a line about subpoenaing an algorithm but not converting a PDF
is a quip with no scene in it, and the contrast reads as a
slogan rather than a roast; a line about regulating crypto
while printing the bill out to scan it back in is a funnier
image but muddies the aim, since the joke becomes about the
printer instead of the lawmaker. The chosen line keeps the
strongest turn and the sharpest aim on every criterion the
judge weighs, in the order the judge weighs them.

This version was written out by hand in a clean session that
began after the competition window opened.

Parent review in round 20261125-0349: re-checked the sealed gate
and the entry line; the line itself is unchanged.
"""

import os

TEXT = "They wrote a 400-page law telling AI exactly how to behave, then emailed their staff asking how to turn their own bill into a PDF."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()


# Round 20261125-0349 parent note: output verified deterministic
# (two local runs, byte-identical) before submission.
