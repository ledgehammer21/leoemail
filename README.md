# Leo Tallahassee lead nurture emails

HTML email examples for Leo Tallahassee, built for Entrata.

| Email | File | Subject line |
| --- | --- | --- |
| Still Interested? | `still-interested.html` | Still Trying to Live Lavishly? |
| See You Tomorrow? | `see-you-tomorrow.html` | Link Up at Leo? |

## Before loading into Entrata

- Images load from this repo (`images/`). Re-upload them to Entrata's asset library and swap the URLs before a live send.
- `*LEAD_NAME_FIRST*` is the Entrata merge field for the lead's first name.
- `0:00 PM` / `0:00 AM` in See You Tomorrow are placeholders for the tour times.
- The Unsubscribe and Manage preferences links in the footer are `#` placeholders. Swap in Entrata's links.

## Editing

Both emails come from one template. Change copy, links or photos in `build/build.py`, then run:

```
python3 build/build.py .
```

`build/assets.py` documents how the images were cut (2x, for a 600px layout).
