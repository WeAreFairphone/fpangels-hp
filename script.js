'use strict'

window.addEventListener('DOMContentLoaded', function() {
  twemoji.parse(document.body)

  const contact_buttons = document.getElementsByClassName('btn-angels')
  for (let button of contact_buttons) {
    const location = button.dataset.location.toLowerCase()
    const mailto = `mailto:${location}@fairphone.community`
    button.setAttribute('href', mailto)
  }
});
