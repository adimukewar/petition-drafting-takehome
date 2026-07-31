# Personal Statement — Ishani Marwah

Crop disease is diagnosed too late. By the time a plant pathologist walks a
field and sees visible symptoms, the infection has usually been spreading for
ten days to three weeks. My work is about closing that gap using imagery that
already exists — drone and satellite multispectral captures that growers are
collecting anyway for other purposes.

The technical obstacle was annotation. Segmentation models want per-pixel
labels, and per-pixel labels for crop disease require a trained pathologist
walking the same field the drone flew. Nobody has that at scale. The datasets
that exist are small, regionally narrow, and inconsistently labeled.

*Lyra*, the method I developed during my postdoc and have continued to extend at
Verdant Systems, trains usable segmentation models from sparse and noisy
annotation — in practice, from a pathologist marking a few dozen points in an
image rather than tracing every lesion. The 2021 paper describing it has been
cited 284 times, and the follow-up work on cross-region transfer addressed the
failure mode that I think had been quietly limiting the field: models trained in
one growing region degrade badly when moved to another, and most published
results did not test for it.

What I am most satisfied by is not the citation count. It is that two
agricultural agencies now run this in production. The Cascadia Regional
Agricultural Board processes its entire seasonal drone survey through *Lyra* and
uses the output to prioritize which fields get a human inspection. Their chief
scientist told me it changed how they allocate inspector time. The Sonoran
Valley authority adopted it the following year for a different crop mix, which
was the real test of whether the transfer work held up outside my own
evaluation.

I lead a group of six at Verdant Systems. My responsibility is the whole path
from research to operational deployment, which in this domain means owning the
question of what the model does when it is wrong — a false negative in a disease
detector means an untreated outbreak, and a false positive means a grower
sprays fungicide they did not need. Getting the calibration right mattered more
to adoption than getting the raw accuracy number up, and that is the part of the
work I would want any assessment of my contribution to focus on.

I intend to continue this work in the United States. The agricultural sensing
ecosystem here — the combination of large-scale operations, established drone
survey practice, and agencies willing to adopt new methods — does not exist in
the same form elsewhere, and the deployments I have built depend on it.

*Ishani Marwah*
*11 May 2026*
