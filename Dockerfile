FROM odoo:17

USER root

RUN pip3 install  opencv-python matplotlib numpy pandas arabic-reshaper attrs beautifulsoup4 cffi charset-normalizer contourpy cycler docopt et-xmlfile 
EXPOSE 8069

ENTRYPOINT ["/entrypoint.sh"]
CMD ["odoo"]
