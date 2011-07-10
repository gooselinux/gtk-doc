Summary: API documentation generation tool for GTK+ and GNOME
Name: gtk-doc
Version: 1.11
Release: 5.1%{?dist}
License: GPLv2+ and GFDL
Group: Development/Tools
Source: http://ftp.gnome.org/pub/GNOME/sources/gtk-doc/1.11/gtk-doc-%{version}.tar.bz2 
# http://bugzilla.gnome.org/show_bug.cgi?id=562064
Patch0: gtk-doc-index.patch
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
URL: http://www.gtk.org/gtk-doc

BuildRequires: docbook-utils 
BuildRequires: jade 
BuildRequires: libxslt 
BuildRequires: docbook-style-xsl
BuildRequires: scrollkeeper
BuildRequires: python
BuildRequires: gnome-doc-utils

Requires(post): scrollkeeper
Requires(postun): scrollkeeper

Requires: docbook-utils jade /usr/bin/cmp libxslt docbook-style-xsl
# we are installing an automake macro
Requires: automake
# we are installing a .pc file
Requires: pkgconfig
# we are installing a .omf file
Requires: scrollkeeper
# we are installing an sgml catalog
Requires: sgml-common

Source1: filter-requires-gtk-doc.sh
%define __perl_requires %{SOURCE1}

%description
gtk-doc is a tool for generating API reference documentation.
It is used for generating the documentation for GTK+, GLib
and GNOME.

%prep

%setup -q
%patch0 -p1 -b .index

# Move this doc file to avoid name collisions
mv doc/README doc/README.docs

%build
%configure --enable-public-id --disable-scrollkeeper
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# --disable-scrollkeeper is not enough
rm -rf $RPM_BUILD_ROOT/var/scrollkeeper

mkdir -p $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html

%clean
rm -rf $RPM_BUILD_ROOT

%post 
scrollkeeper-update -q

%postun
scrollkeeper-update -q

%files
%defattr(-, root, root)
%doc AUTHORS README doc/* examples COPYING COPYING-DOCS
%{_bindir}/*
%{_datadir}/aclocal/gtk-doc.m4
%{_datadir}/gtk-doc/
%{_datadir}/sgml/gtk-doc/
%{_datadir}/pkgconfig/gtk-doc.pc
%{_datadir}/gnome/help/gtk-doc-manual/
%{_datadir}/omf/gtk-doc-manual

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.11-5.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 23 2008 Matthias Clasen <mclasen@redhat.com> - 1.11-3
- Fix an index generation problem

* Fri Nov 21 2008 Matthias Clasen <mclasen@redhat.com> - 1.11-2
- Update to 1.11

* Fri Jul 25 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.10-2
- fix license tag

* Thu Apr 24 2008 Matthias Clasen <mclasen@redhat.com> - 1.10-1
- Update to 1.10

* Tue Jan  8 2008 Matthias Clasen <mclasen@redhat.com> - 1.9-4
- Try again 

* Mon Jan  7 2008 Matthias Clasen <mclasen@redhat.com> - 1.9-3
- Improve the fix 

* Tue Dec 18 2007 Matthias Clasen <mclasen@redhat.com> - 1.9-2
- Fix a problem in gtk-doc.make

* Sun Nov 18 2007 Matthias Clasen <mclasen@redhat.com> - 1.9-1
- Update to 1.9

* Tue Aug  7 2007 Matthias Clasen <mclasen@redhat.com> - 1.8-3
- Update the license field

* Thu Mar 29 2007 Matthias Clasen <mclasen@redhat.com> - 1.8-2
- Drop a no longer needed patch

* Wed Feb 21 2007 Matthias Clasen <mclasen@redhat.com> - 1.8-1
- Update to 1.8
- Fix some directory ownership issues

* Fri Feb  2 2007 Matthias Clasen <mclasen@redhat.com> - 1.7-3
- Fix the omf file (#223684)

* Wed Dec 20 2006 Matthias Clasen <mclasen@redhat.com> - 1.7-2
- Own the /usr/share/gtk-doc/html directory (#220230)

* Wed Aug  2 2006 Matthias Clasen <mclasen@redhat.com> - 1.7-1.fc6
- Update to 1.7

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.6-3.1
- rebuild

* Mon May 22 2006 Matthias Clasen <mclasen@redhat.com> 1.6-3
- Make it build in mock

* Mon Apr 10 2006 Matthias Clasen <mclasen@redhat.com> 1.6-2
- Update to 1.6

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Jul  6 2005 Matthias Clasen <mclasen@redhat.com> 1.4-1
- update to 1.4

* Thu May  5 2005 Matthias Clasen <mclasen@redhat.com> 1.3-1
- accept ':' in ids

* Wed Jan 26 2005 Matthias Clasen <mclasen@redhat.com> 1.3-1
- update to 1.3

* Tue Sep 21 2004 Matthias Clasen <mclasen@redhat.com> 1.2-2
- rebuild 

* Fri Mar 12 2004 Alex Larsson <alexl@redhat.com> 1.2-1
- update to 1.2

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Aug 28 2003 Owen Taylor <otaylor@redhat.com> 1.1-3.0
- Move gtk-doc.pc file to %%{_datadir}/pkgconfig (#98595)
- Require: /usr/bin/cmp (#88763, Thomas Vander Stichele)
- Added libxslt docbook-style-xsl to Require: and BuildPrereq
  (#99143, Ken MacFarlane)

* Tue Jul  8 2003 Owen Taylor <otaylor@redhat.com> 1.1-2.0
- Bump for rebuild

* Thu Jun 12 2003 Owen Taylor <otaylor@redhat.com> 1.1-1
- Version 1.1

* Wed Apr 30 2003 Elliot Lee <sopwith@redhat.com> 0.10-6
- Patch to s/head -1/head -n 1/ for ppc64 etc.

* Wed Feb 12 2003 Elliot Lee <sopwith@redhat.com> 0.10-5
- BuildRequires: libxslt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Jan 13 2003 Owen Taylor <otaylor@redhat.com> 0.10-3
- Clean up some spec file mess

* Mon Jan 13 2003 Tim Powers <timp@redhat.com> 0.10-2
- fiter out the broken perl dep

* Sun Jan 12 2003 Havoc Pennington <hp@redhat.com>
- 0.10

* Wed Dec 11 2002 Tim Powers <timp@redhat.com> 0.9-6
- rebuild

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 30 2002 Chip Turner <cturner@redhat.com>
- add dependency filter for bogus perl dependencies

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu Apr 25 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Thu Apr  4 2002 Jeremy Katz <katzj@redhat.com>
- update to 0.9

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- new cvs snap 0.7.90

* Mon Sep 17 2001 Matt Wilson <msw@redhat.com>
- version 0.7

* Thu May 17 2001 Havoc Pennington <hp@redhat.com>
- upgrade to a CVS snapshot
- remove patches applied upstream

* Tue Jan 16 2001 Tim Waugh <twaugh@redhat.com>
- Replace docbook, sgml-common, and stylesheets requirements with
  docbook-utils requirement.
- Use public identifier in custom stylesheets.

* Thu Dec 14 2000 Bill Nottingham <notting@redhat.com>
- rebuild because of broken fileutils

* Mon Nov 13 2000 Owen Taylor <otaylor@redhat.com>
- Version 0.4b1 (CVS snapshot)

* Fri Apr 23 1999 Owen Taylor <otaylor@redhat.com>
- added Requires

* Fri Apr 23 1999 Owen Taylor <otaylor@redhat.com>
- Initial RPM, version 0.2

