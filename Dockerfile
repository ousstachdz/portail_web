FROM odoo:17

USER root

EXPOSE 8069

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]
