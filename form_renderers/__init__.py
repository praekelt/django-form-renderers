def as_div(form):
    """This formatter arranges label, widget, help text and error messages by
    using divs."""

    # Yes, evil but the easiest way to set this property for all forms.
    form.required_css_class = "Field-Required"

    return form._html_output(
        normal_row=u"""<div class="Field">%(label)s<div %(html_class_attr)s>%(errors)s %(field)s</div><div class="helptext">%(help_text)s</div></div>""",
        error_row=u"%s",
        row_ender="</div>",
        help_text_html=u"%s",
        errors_on_separate_row=False
    )
