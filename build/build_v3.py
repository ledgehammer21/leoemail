"""V3: an alternate, action-first design for the Leo Tallahassee lead-nurture emails."""
import sys, os
from urllib.parse import quote

OUT = sys.argv[1]
IMG = 'https://raw.githubusercontent.com/ledgehammer21/leoemail/main/images/'

SITE = 'https://www.leotallahassee.com/'
FLOOR_PLANS = SITE + 'floor-plans/'
AMENITIES = SITE + 'amenities/'
CONTACT = SITE + 'contact/'
APPLY = 'https://leotally.prospectportal.com/Apartments/module/application_authentication/'
TEL = 'tel:+18502205585'
SMS = 'sms:+18502205585'
EMAIL = 'info@leotallahassee.com'

PINK, TEAL, CHAR = '#f39391', '#3f6d78', '#3b3735'
SERIF = "'The Seasons','Playfair Display',Georgia,'Times New Roman',serif"
SANS = "'Figtree','Helvetica Neue',Helvetica,Arial,sans-serif"
FOOT_SANS = "'Open Sans','Helvetica Neue',Helvetica,Arial,sans-serif"
LEAF = 'border-radius:36px 0 36px 0;'
LEAF_SM = 'border-radius:24px 0 24px 0;'


def reply(subject, body):
    """One-tap reply: opens a pre-written email to the leasing team."""
    return f'mailto:{EMAIL}?subject={quote(subject)}&amp;body={quote(body)}'


def eyebrow(text, color):
    return (f'<p style="margin:0 0 10px 0;font-family:{SANS};font-size:12px;line-height:16px;font-weight:500;'
            f'letter-spacing:2.5px;text-transform:uppercase;color:{color};">{text}</p>')


def button(label, href, bg, fg, border=None):
    b = f'border:1px solid {border};' if border else f'border:1px solid {bg};'
    return (f'<td class="stack" width="47.9%" align="center" bgcolor="{bg}" style="background-color:{bg};{b}{LEAF_SM}">'
            f'<a href="{href}" style="display:block;padding:12px 6px;font-family:{SANS};font-size:16px;line-height:24px;'
            f'font-weight:500;color:{fg};text-decoration:none;white-space:nowrap;">{label}</a></td>')


def slot_card(day, time, note, href, bg, fg, sub):
    return f'''<td class="stack" width="47.9%" valign="top" bgcolor="{bg}" style="background-color:{bg};{LEAF}">
            <a href="{href}" style="display:block;padding:26px 24px 24px 24px;text-decoration:none;color:{fg};">
              <span style="display:block;font-family:{SANS};font-size:11px;line-height:16px;font-weight:500;letter-spacing:2.5px;text-transform:uppercase;color:{sub};">{day}</span>
              <span style="display:block;padding:6px 0 8px 0;font-family:{SERIF};font-size:42px;line-height:46px;font-weight:400;color:{fg};white-space:nowrap;">{time}</span>
              <span style="display:block;font-family:{SANS};font-size:15px;line-height:21px;font-weight:300;color:{fg};">{note}</span>
              <span style="display:block;padding-top:18px;font-family:{SANS};font-size:15px;line-height:21px;font-weight:500;color:{fg};text-decoration:underline;">Book this one &rarr;</span>
            </a>
          </td>'''


GAP = '<td class="stack-gap" width="4.2%" style="font-size:0;line-height:0;">&nbsp;</td>'


def tour_action():
    return f'''
  <!-- ACTION: two one-tap tour slots -->
  <tr>
    <td class="px" style="padding:0 40px 14px 40px;background-color:#ffffff;" bgcolor="#ffffff">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          {slot_card('Today', '0:00 PM', 'No time better than the present!', reply('Tour today at 0:00 PM', 'Hi Leo Tally Team, put me down for a tour today at 0:00 PM!'), PINK, CHAR, CHAR)}
          {GAP}
          {slot_card('Tomorrow', '0:00 AM', 'Sleep on it, then come see it.', reply('Tour tomorrow at 0:00 AM', 'Hi Leo Tally Team, put me down for a tour tomorrow at 0:00 AM!'), TEAL, '#ffffff', '#d6e3e6')}
        </tr>
      </table>
    </td>
  </tr>
  <tr>
    <td class="px" style="padding:10px 40px 44px 40px;background-color:#ffffff;" bgcolor="#ffffff">
      <p style="margin:0;font-family:{SANS};font-size:16px;line-height:24px;font-weight:300;color:{TEAL};">If neither works, just text us at <a href="{SMS}" style="color:{TEAL};font-weight:500;text-decoration:underline;white-space:nowrap;">(850) 220-5585</a> and we&rsquo;ll find a time that does.</p>
    </td>
  </tr>'''


def still_action():
    return f'''
  <!-- ACTION: urgency card with a one-tap reply -->
  <tr>
    <td class="px" style="padding:0 40px 30px 40px;background-color:#ffffff;" bgcolor="#ffffff">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td class="card" background="{IMG}pattern-pink.png" bgcolor="#f39694" style="padding:34px 32px 34px 32px;background-color:#f39694;background-image:url('{IMG}pattern-pink.png');background-repeat:repeat;background-size:100px 100px;{LEAF}">
            <p style="margin:0 0 10px 0;font-family:{SERIF};font-size:32px;line-height:36px;font-weight:400;color:{CHAR};">Spots are starting to&nbsp;fill,</p>
            <p style="margin:0 0 24px 0;font-family:{SANS};font-size:17px;line-height:25px;font-weight:400;color:{CHAR};">and it would make us (and you, we&rsquo;re sure) super sad if you missed out on the floor plan of your dreams.</p>
            <table role="presentation" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td align="center" bgcolor="{CHAR}" style="background-color:{CHAR};{LEAF_SM}">
                  <a href="{reply('Tell me more', 'Tell me more!')}" style="display:block;padding:13px 30px;font-family:{SANS};font-size:17px;line-height:24px;font-weight:500;color:#ffffff;text-decoration:none;white-space:nowrap;">Tell me more &rarr;</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </td>
  </tr>'''


def still_contact():
    return f'''
  <!-- CONTACT -->
  <tr>
    <td class="px" style="padding:34px 40px 0 40px;background-color:#ffffff;" bgcolor="#ffffff">
      <p style="margin:0 0 20px 0;font-family:{SANS};font-size:16px;line-height:24px;font-weight:300;color:{TEAL};">Give us a call or send us a message...we&rsquo;re around every day from 10-5. Heck, you can even reply to this email with a simple &ldquo;tell me more.&rdquo;</p>
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          {button('Call (850) 220-5585', TEL, TEAL, '#ffffff')}
          {GAP}
          {button('Send a Message', CONTACT, '#ffffff', TEAL, TEAL)}
        </tr>
      </table>
    </td>
  </tr>'''


def build(e):
    return f'''<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="x-apple-disable-message-reformatting">
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
<meta name="color-scheme" content="light only">
<meta name="supported-color-schemes" content="light only">
<title>{e['subject']}</title>
<!-- Subject line: {e['subject']} -->
<!--[if mso]>
<noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript>
<style>td,th,div,p,a,h1,h2,h3,span {{font-family: Georgia, Arial, sans-serif;}}</style>
<![endif]-->
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@300;400;500&family=Open+Sans:wght@400;700&family=Playfair+Display:wght@400&display=swap" rel="stylesheet">
<style>
  :root {{ color-scheme: light only; }}
  body {{ margin:0; padding:0; width:100% !important; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%; }}
  table {{ border-collapse:separate; mso-table-lspace:0; mso-table-rspace:0; }}
  img {{ -ms-interpolation-mode:bicubic; }}
  a[x-apple-data-detectors] {{ color:inherit !important; text-decoration:none !important; }}
  @media only screen and (max-width:620px) {{
    .wrap {{ width:100% !important; }}
    .px {{ padding-left:24px !important; padding-right:24px !important; }}
    .card {{ padding-left:24px !important; padding-right:24px !important; }}
    .stack {{ display:block !important; width:auto !important; }}
    .stack-gap {{ display:block !important; width:100% !important; height:14px !important; line-height:14px !important; }}
    .h1 {{ font-size:32px !important; line-height:36px !important; }}
    .nav a {{ padding:0 8px !important; }}
  }}
</style>
</head>
<body style="margin:0;padding:0;background-color:#f3efec;">

<!-- Preheader (inbox preview text) -->
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:#f3efec;opacity:0;">{e['preheader']}&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;</div>

<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="#f3efec" style="background-color:#f3efec;">
<tr><td align="center">

<table role="presentation" class="wrap" width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" style="width:600px;max-width:600px;background-color:#ffffff;">

  <!-- HEADER -->
  <tr>
    <td style="font-size:0;line-height:0;background-color:#e4605a;" bgcolor="#e4605a">
      <a href="{SITE}" target="_blank" style="text-decoration:none;"><img src="{IMG}{e.get('header','header.jpg')}" width="600" height="{e.get('header_h',276)}" alt="Leo Tallahassee" style="display:block;width:100%;max-width:600px;height:auto;border:0;outline:none;font-family:Georgia,serif;font-size:40px;line-height:{e.get('header_h',276)}px;color:#ffffff;text-align:center;"></a>
    </td>
  </tr>

  <!-- INTRO -->
  <tr>
    <td class="px" style="padding:46px 40px 30px 40px;background-color:#ffffff;" bgcolor="#ffffff">
      {eyebrow('Hi *LEAD_NAME_FIRST*,', '#e4605a')}
      <h1 class="h1" style="margin:0 0 18px 0;font-family:{SERIF};font-size:40px;line-height:44px;font-weight:400;color:{TEAL};">{e['headline']}</h1>
      <p style="margin:0;font-family:{SANS};font-size:17px;line-height:26px;font-weight:300;color:{TEAL};">{e['intro']}</p>
    </td>
  </tr>
{e['action']}

  <!-- MOSAIC -->
  <tr>
    <td class="px" style="padding:0 40px 0 40px;background-color:#ffffff;" bgcolor="#ffffff">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td width="47.9%" valign="top" style="font-size:0;line-height:0;"><a href="{e['tall'][2]}" target="_blank"><img src="{IMG}{e['tall'][0]}" width="249" height="330" alt="{e['tall'][1]}" style="display:block;width:100%;max-width:249px;height:auto;border:0;"></a></td>
          <td width="4.2%" style="font-size:0;line-height:0;">&nbsp;</td>
          <td width="47.9%" valign="top" style="font-size:0;line-height:0;"><a href="{e['pair'][2]}" target="_blank"><img src="{IMG}{e['pair'][0]}" width="249" height="330" alt="{e['pair'][1]}" style="display:block;width:100%;max-width:249px;height:auto;border:0;"></a></td>
        </tr>
      </table>
    </td>
  </tr>
{e.get('after', '')}
  <!-- SIGN-OFF -->
  <tr>
    <td class="px" style="padding:38px 40px 48px 40px;background-color:#ffffff;" bgcolor="#ffffff">
      <h2 style="margin:0 0 20px 0;font-family:{SERIF};font-size:27px;line-height:34px;font-weight:400;color:{TEAL};">{e['closing']}</h2>
      <p style="margin:0;font-family:{SANS};font-size:17px;line-height:25px;font-weight:300;color:{TEAL};">{e['signoff']}<br>Leo Tally Team</p>
    </td>
  </tr>

  <!-- FOOTER -->
  <tr>
    <td class="px" align="center" bgcolor="{CHAR}" style="padding:48px 30px 42px 30px;background-color:{CHAR};">
      <p style="margin:0 0 26px 0;font-family:{SERIF};font-size:26px;line-height:32px;font-weight:400;color:#ffffff;"><span style="color:#f8b5b3;">L</span>iterally <span style="color:#f8b5b3;">E</span>veryone&rsquo;s <span style="color:#f8b5b3;">O</span>bsessed</p>
      <p class="nav" style="margin:0 0 24px 0;font-family:{FOOT_SANS};font-size:11px;line-height:18px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#ffffff;">
        <a href="{FLOOR_PLANS}" target="_blank" style="color:#ffffff;text-decoration:underline;padding:0 12px;white-space:nowrap;">Floor Plans</a>
        <a href="{AMENITIES}" target="_blank" style="color:#ffffff;text-decoration:underline;padding:0 12px;white-space:nowrap;">Amenities</a>
        <a href="{APPLY}" target="_blank" style="color:#ffffff;text-decoration:underline;padding:0 12px;white-space:nowrap;">Apply Now</a>
      </p>
      <p style="margin:0 0 30px 0;font-family:{FOOT_SANS};font-size:12px;line-height:20px;font-weight:400;color:#ffffff;">
        Leasing Office: 603 W Gaines Street, Unit 1, <span style="white-space:nowrap;">Tallahassee, FL 32310</span><br>
        Community: 699 W. Tennessee St., <span style="white-space:nowrap;">Tallahassee, FL 32304</span><br>
        <a href="{TEL}" style="color:#ffffff;text-decoration:underline;">(850) 220-5585</a> &middot; <a href="mailto:{EMAIL}" style="color:#ffffff;text-decoration:underline;">{EMAIL}</a>
      </p>
      <!-- ENTRATA: swap the two # links below for Entrata's unsubscribe / preferences merge links -->
      <p style="margin:0;font-family:{FOOT_SANS};font-size:11px;line-height:18px;font-weight:400;color:#c9c5c2;">
        <a href="#" style="color:#c9c5c2;text-decoration:underline;">Unsubscribe</a> &middot; <a href="#" style="color:#c9c5c2;text-decoration:underline;">Manage preferences</a>
      </p>
    </td>
  </tr>

</table>

</td></tr>
</table>
</body>
</html>
'''


EMAILS = {
    'v3-see-you-tomorrow.html': dict(
        subject='Link Up at Leo?',
        preheader='Two tour openings, one tap to book. Pick the time that works best.',
        headline='Let&rsquo;s get a tour of Leo Tallahassee on your calendar!',
        intro='We have two tour openings. Tap the time that works best, hit send, and we&rsquo;ll get you on the calendar!',
        action=tour_action(),
        header='header-short.jpg', header_h=180,
        tall=('v3-tour-tall.jpg', 'Rooftop pool and sun deck from above', AMENITIES),
        pair=('v3-tour-stack.jpg', 'The Leo Tallahassee leasing entrance, and friends taking a gameday selfie', CONTACT),
        closing='We can&rsquo;t wait to meet you and show you what living lavishly at Leo looks like.',
        signoff='See you soon,',
    ),
    'v3-still-interested.html': dict(
        subject='Still Trying to Live Lavishly?',
        preheader='Spots are starting to fill. Let&rsquo;s find the floor plan of your dreams.',
        headline='Still thinking about making Leo your home next year?',
        intro='We&rsquo;d love to chat and help you see why Literally Everyone&rsquo;s Obsessed with Leo. We&rsquo;re happy to '
              'answer any questions about floor plans, availability, or the leasing process!',
        action=still_action(),
        after=still_contact(),
        header='header-short.jpg', header_h=180,
        tall=('v3-still-tall.jpg', 'Two friends with iced coffees outside a coffee shop', SITE),
        pair=('v3-still-stack.jpg', 'Rooftop pool with a Jumbotron, and a resident smiling poolside', AMENITIES),
        closing='We&rsquo;re here to help!',
        signoff='Talk soon,',
    ),
}

for name, e in EMAILS.items():
    with open(os.path.join(OUT, name), 'w') as f:
        f.write(build(e))
    print('wrote', name)
