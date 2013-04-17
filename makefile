# Copyright © 2013 Martin Ueding <dev@martin-ueding.de>

all: type-speed.1.gz

install:
	install -d "$(DESTDIR)/usr/bin"
	install type-speed -t "$(DESTDIR)/usr/bin"
	install -d "$(DESTDIR)/usr/share/man/man1"
	install type-speed.1.gz -t "$(DESTDIR)/usr/share/man/man1"

%.1: %.1.rst
	rst2man $< $@

%.1.gz: %.1
	gzip $<

.PHONY: clean
clean:
	$(RM) *.class *.jar
	$(RM) *.o *.out
	$(RM) *.pyc *.pyo
	$(RM) *.orig
