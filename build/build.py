"""Builds the Leo Tallahassee lead-nurture emails from one shared template."""
import sys, os, html

OUT = sys.argv[1]
IMG = 'https://raw.githubusercontent.com/ledgehammer21/leoemail/main/images/'

SITE = 'https://www.leotallahassee.com/'
FLOOR_PLANS = SITE + 'floor-plans/'
AMENITIES = SITE + 'amenities/'
CONTACT = SITE + 'contact/'
APPLY = 'https://leotally.prospectportal.com/Apartments/module/application_authentication/'
TEL = 'tel:+18502205585'
SMS = 'sms:18502205585?&body=LEOTALLY'
MAIL = 'mailto:info@leotallahassee.com'

PINK, TEAL, CHAR = '#f39391', '#3f6d78', '#3b3735'
SERIF = "'The Seasons','Playfair Display',Georgia,'Times New Roman',serif"
SANS = "'Figtree','Helvetica Neue',Helvetica,Arial,sans-serif"
FOOT_SERIF = "'Playfair Display',Georgia,'Times New Roman',serif"
FOOT_SANS = "'Open Sans','Helvetica Neue',Helvetica,Arial,sans-serif"


def photo_block(big, left, right, pad_top, pad_bottom):
    def img(p, w, h):
        return (f'<a href="{p[2]}" target="_blank" style="text-decoration:none;">'
                f'<img src="{IMG}{p[0]}" width="{w}" height="{h}" alt="{html.escape(p[1])}" '
                f'style="display:block;width:100%;max-width:{w}px;height:auto;border:0;outline:none;"></a>')
    return f'''
  <!-- PHOTOS -->
  <tr>
    <td class="px" style="padding:{pad_top}px 100px {pad_bottom}px 100px;background-color:#ffffff;" bgcolor="#ffffff">
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td colspan="3" style="padding:0 0 22px 0;font-size:0;line-height:0;">{img(big, 400, 216)}</td>
        </tr>
        <tr>
          <td width="47.25%" valign="top" style="font-size:0;line-height:0;">{img(left, 189, 216)}</td>
          <td width="5.5%" style="font-size:0;line-height:0;">&nbsp;</td>
          <td width="47.25%" valign="top" style="font-size:0;line-height:0;">{img(right, 189, 216)}</td>
        </tr>
      </table>
    </td>
  </tr>'''


def build(e):
    body_paras = ''.join(
        f'<p style="margin:0 0 0 0;font-family:{SANS};font-size:17px;line-height:25px;font-weight:300;color:{TEAL};">{p}</p>'
        for p in e['intro'])
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
<style>td,th,div,p,a,h1,h2,h3 {{font-family: Georgia, Arial, sans-serif;}}</style>
<![endif]-->
<link href="https://fonts.googleapis.com/css2?family=Figtree:wght@300;400;500&family=Open+Sans:wght@400;700&family=Playfair+Display:wght@400&display=swap" rel="stylesheet">
<style>
  :root {{ color-scheme: light only; }}
  body {{ margin:0; padding:0; width:100% !important; -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%; }}
  table {{ border-collapse:collapse; mso-table-lspace:0; mso-table-rspace:0; }}
  img {{ -ms-interpolation-mode:bicubic; }}
  a {{ color:inherit; }}
  a[x-apple-data-detectors] {{ color:inherit !important; text-decoration:none !important; }}
  @media only screen and (max-width:620px) {{
    .wrap {{ width:100% !important; }}
    .px {{ padding-left:24px !important; padding-right:24px !important; }}
    .btn-cell {{ display:block !important; width:100% !important; }}
    .btn-gap {{ display:block !important; width:100% !important; height:14px !important; line-height:14px !important; }}
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
      <a href="{SITE}" target="_blank" style="text-decoration:none;"><img src="{IMG}header.jpg" width="600" height="276" alt="Leo Tallahassee" style="display:block;width:100%;max-width:600px;height:auto;border:0;outline:none;font-family:{FOOT_SERIF};font-size:40px;line-height:276px;color:#ffffff;text-align:center;"></a>
    </td>
  </tr>

  <!-- INTRO -->
  <tr>
    <td class="px" style="padding:44px 100px 0 100px;background-color:#ffffff;" bgcolor="#ffffff">
      <p style="margin:0 0 24px 0;font-family:{SERIF};font-size:26px;line-height:32px;font-weight:400;color:{PINK};">Hi *LEAD_NAME_FIRST*,</p>
      <h1 style="margin:0 0 30px 0;font-family:{SERIF};font-size:21px;line-height:25px;font-weight:400;color:{PINK};">{e['headline']}</h1>
      {body_paras}
    </td>
  </tr>
{photo_block(*e['photos_top'], 42, 45)}

  <!-- TEAL BAND -->
  <tr>
    <td class="px" background="{IMG}pattern-teal.png" bgcolor="#44717c" style="padding:98px 100px 100px 100px;background-color:#44717c;background-image:url('{IMG}pattern-teal.png');background-repeat:repeat;background-position:top left;background-size:100px 100px;">
      <p style="margin:0;font-family:{SANS};font-size:17px;line-height:25px;font-weight:300;color:#ffffff;">{e['teal']}</p>
    </td>
  </tr>
{photo_block(*e['photos_bottom'], 45, 45)}

  <!-- PINK BAND + BUTTONS -->
  <tr>
    <td class="px" background="{IMG}pattern-pink.png" bgcolor="#f39694" style="padding:62px 100px 70px 100px;background-color:#f39694;background-image:url('{IMG}pattern-pink.png');background-repeat:repeat;background-position:top left;background-size:100px 100px;">
      <p style="margin:0 0 44px 0;font-family:{SANS};font-size:17px;line-height:25px;font-weight:400;color:#ffffff;">{e['pink']}</p>
      <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
        <tr>
          <td class="btn-cell" width="47.25%" align="center" bgcolor="{CHAR}" style="background-color:{CHAR};border-radius:24px 0 24px 0;">
            <a href="{TEL}" style="display:block;padding:12px 6px;font-family:{SANS};font-size:17px;line-height:25px;font-weight:400;color:#ffffff;text-decoration:none;white-space:nowrap;">Call (850) 220-5585</a>
          </td>
          <td class="btn-gap" width="5.5%" style="font-size:0;line-height:0;">&nbsp;</td>
          <td class="btn-cell" width="47.25%" align="center" bgcolor="#ffffff" style="background-color:#ffffff;border-radius:24px 0 24px 0;">
            <a href="{CONTACT}" target="_blank" style="display:block;padding:12px 6px;font-family:{SANS};font-size:17px;line-height:25px;font-weight:500;color:{CHAR};text-decoration:none;white-space:nowrap;">Send a Message</a>
          </td>
        </tr>
      </table>
    </td>
  </tr>

  <!-- SIGN-OFF -->
  <tr>
    <td class="px" style="padding:34px 100px 46px 100px;background-color:#ffffff;" bgcolor="#ffffff">
      <h2 style="margin:0 0 26px 0;font-family:{SERIF};font-size:27px;line-height:34px;font-weight:400;color:{TEAL};">{e['closing']}</h2>
      <p style="margin:0;font-family:{SANS};font-size:17px;line-height:25px;font-weight:300;color:{TEAL};">{e['signoff']}<br>Leo Tally Team</p>
    </td>
  </tr>

  <!-- FOOTER -->
  <tr>
    <td class="px" align="center" bgcolor="{CHAR}" style="padding:52px 30px 44px 30px;background-color:{CHAR};">
      <p style="margin:0 0 28px 0;font-family:{FOOT_SERIF};font-size:22px;line-height:30px;font-weight:400;color:#ffffff;">Literally Everyone&rsquo;s Obsessed</p>
      <p class="nav" style="margin:0 0 26px 0;font-family:{FOOT_SANS};font-size:11px;line-height:18px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#ffffff;">
        <a href="{FLOOR_PLANS}" target="_blank" style="color:#ffffff;text-decoration:underline;padding:0 12px;white-space:nowrap;">Floor Plans</a>
        <a href="{AMENITIES}" target="_blank" style="color:#ffffff;text-decoration:underline;padding:0 12px;white-space:nowrap;">Amenities</a>
        <a href="{APPLY}" target="_blank" style="color:#ffffff;text-decoration:underline;padding:0 12px;white-space:nowrap;">Apply Now</a>
      </p>
      <p style="margin:0 0 36px 0;font-family:{FOOT_SANS};font-size:12px;line-height:20px;font-weight:400;color:#ffffff;">
        Leasing Office: 603 W Gaines Street, Unit 1, <span style="white-space:nowrap;">Tallahassee, FL 32310</span><br>
        Community: 699 W. Tennessee St., <span style="white-space:nowrap;">Tallahassee, FL 32304</span><br>
        <a href="{TEL}" style="color:#ffffff;text-decoration:underline;">(850) 220-5585</a> &middot; <a href="{MAIL}" style="color:#ffffff;text-decoration:underline;">info@leotallahassee.com</a>
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


EXT = ('exterior-entry.jpg', 'The Leo Tallahassee leasing entrance', CONTACT)
KIT = ('kitchen.jpg', 'Apartment kitchen with island seating', FLOOR_PLANS)
POOLA = ('pool-aerial.jpg', 'Rooftop pool and sun deck from above', AMENITIES)
POOL = ('rooftop-pool.jpg', 'Rooftop pool with a Jumbotron and loungers', AMENITIES)
LIV = ('living-room.jpg', 'Furnished apartment living room', FLOOR_PLANS)
PICK = ('pickleball-court.jpg', 'Indoor pickleball court', AMENITIES)
F1 = ('friends-campus.jpg', 'Friends walking through campus', SITE)
F2 = ('friends-pickleball.jpg', 'Three friends with a pickleball paddle', SITE)
F3 = ('friends-selfie.jpg', 'Two friends taking a selfie', SITE)
G1 = ('friends-gameday-selfie.jpg', 'Friends in garnet and gold taking a group selfie', SITE)
G2 = ('friends-coffee.jpg', 'Two friends with iced coffees outside a coffee shop', SITE)
G3 = ('poolside.jpg', 'Smiling by the pool in sunglasses', AMENITIES)

EMAILS = {
    'still-interested.html': dict(
        subject='Still Trying to Live Lavishly?',
        preheader='Spots are starting to fill. Let&rsquo;s find the floor plan of your dreams.',
        headline='Still thinking about making Leo your home next year?',
        intro=['We&rsquo;d love to chat and help you see why Literally Everyone&rsquo;s Obsessed with Leo. '
               'We&rsquo;re happy to answer any questions about floor plans, availability, or the leasing process!'],
        photos_top=(POOL, LIV, PICK),
        teal='Spots are starting to fill, and it would make us (and you, we&rsquo;re sure) super sad if you '
             'missed out on the floor plan of your dreams.',
        photos_bottom=(G1, G2, G3),
        pink='Give us a call or send us a message...we&rsquo;re around every day from 10-5. Heck, you can even '
             'reply to this email with a simple &ldquo;tell me more.&rdquo;',
        closing='We&rsquo;re here to help!',
        signoff='Talk soon,',
    ),
    'see-you-tomorrow.html': dict(
        subject='Link Up at Leo?',
        preheader='Tour openings today and tomorrow. Reply with the time that works best.',
        headline='Let&rsquo;s get a tour of Leo Tallahassee<br>on your calendar!',
        intro=['We have tour openings today at 0:00 PM (no time better than the present!) or tomorrow at 0:00 AM.'],
        photos_top=(EXT, KIT, POOLA),
        teal='Reply with the time that works best, and we&rsquo;ll get you on the calendar! If neither works, '
             'just text us at <a href="' + SMS + '" style="color:#ffffff;text-decoration:none;white-space:nowrap;">(850) 220-5585</a> '
             'and we&rsquo;ll find a time that does.',
        photos_bottom=(F1, F2, F3),
        pink='We can&rsquo;t wait to meet you and show you what living lavishly at Leo looks like.',
        closing='We&rsquo;re here to help!',
        signoff='Talk soon,',
    ),
}

for name, e in EMAILS.items():
    with open(os.path.join(OUT, name), 'w') as f:
        f.write(build(e))
    print('wrote', name)
