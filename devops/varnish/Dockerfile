# syntax=docker/dockerfile:1
FROM varnish:7.6

LABEL maintainer="Ivan Codarin <ivan.codarin@gmail.com>" \
      org.label-schema.name="ploneconf2025-varnish" \
      org.label-schema.description="Plone Conference Training Varnish image." \
      org.label-schema.vendor="Ivan Codarin"

COPY etc/varnish.vcl /etc/varnish/default.vcl
