###############################################################################
# Sloan Digital Sky Survey IV (SDSS-IV)
# Code for product: Actorkeys
#
# This Makefile & all Makefiles in this product are GNU make compliant.
# Please help keep them that way.  See
# http://www.gnu.org/software/make/manual/make.html
#
# $Id$
#
###############################################################################
#
# Change INSTALL_DIR here!
#
INSTALL_DIR = $(ACTORKEYS_DIR)
#
# Use this shell to interpret shell commands, & pass its value to sub-make
#
export SHELL = /bin/sh
#
# This is like doing 'make -w' on the command line.  This tells make to
# print the directory it is in.
#
MAKEFLAGS = w
#
# This is a list of subdirectories that make should descend into.  Makefiles
# in these subdirectories should also understand 'make all' & 'make clean'.
# This list can be empty, but should still be defined.
#
SUBDIRS = python/actorkeys
#
# This line helps prevent make from getting confused in the case where you
# have a file named 'clean'.
#
.PHONY : clean
#
# This should compile all code prior to it being installed
#
all :
	for f in $(SUBDIRS); do $(MAKE) -C $$f all ; done

#
# GNU make pre-defines $(RM).  The - in front of $(RM) causes make to
# ignore any errors produced by $(RM).
#
clean :
	- $(RM) *~ core
	@ for f in $(SUBDIRS); do $(MAKE) -C $$f clean ; done

