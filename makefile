# Copyright © 2013, 2016 Martin Ueding <dev@martin-ueding.de>

all: type-speed.1.gz

install:
	install -d "$(DESTDIR)/usr/bin"
	install type_speed.py -t "$(DESTDIR)/usr/bin"
	install -d "$(DESTDIR)/usr/share/man/man1"
	install type-speed.1.gz -t "$(DESTDIR)/usr/share/man/man1"

%.1: %.1.rst
	rst2man $< $@

%.1.gz: %.1
	gzip $<

.PHONY: clean
clean:
	$(RM) *.1
	$(RM) *.1.gz
	$(RM) *.class *.jar
	$(RM) *.o *.out
	$(RM) *.orig
	$(RM) *.pyc *.pyo
