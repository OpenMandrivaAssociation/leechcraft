Name:		leechcraft
Version:	0.5.97
Release:	1
Summary:	Modular Internet Client
License:	GPLv3+
Group:		Networking/Other
Url:		http://leechcraft.org
Source0:	http://netcologne.dl.sourceforge.net/project/%{name}/LeechCraft/%{version}/%{name}-%{version}.tar.xz
Patch0:		leechcraft-0.5.97-linkage.patch
Patch1:		leechcraft-0.5.97-soname.patch
BuildRequires:	cmake
BuildRequires:	boost-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	liblastfm-devel
BuildRequires:	lm_sensors-devel
BuildRequires:	magic-devel
BuildRequires:	qt4-devel
BuildRequires:	qwt-devel
BuildRequires:	pkgconfig(ddjvuapi)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	pkgconfig(libchromaprint)
BuildRequires:	pkgconfig(libnl-3.0)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(libspectre)
BuildRequires:	pkgconfig(libtorrent-rasterbar)
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(poppler-qt4)
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(qxmpp)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xscrnsaver)
# Core modules:
Requires:	%{name}-cstp = %{EVRD}
Requires:	%{name}-sb2 = %{EVRD}
Requires:	%{name}-summary = %{EVRD}
Requires:	%{name}-tabsessmanager = %{EVRD}
Requires:	%{name}-tpi = %{EVRD}
Suggests:	%{name}-plugins-main = %{EVRD}

%description
LeechCraft is a free modular "Internet client" application.

LeechCraft allows to browse the web, read RSS/Atom feeds, download
files via BitTorrent, HTTP, FTP and DC, automatically stream,
download or play podcasts and other media files and much more.

Features can be easily added via plugins that can be integrated with
each other with no effert while staying abstract from the exact
implementation.

This package contains the main LeechCraft executable, which connects
all the plugins with each other, routes requests between them, tracks
dependencies and performs several other housekeeping tasks.

%files -f %{name}.lang
%{_bindir}/leechcraft
%{_bindir}/leechcraft-add-file
%{_bindir}/leechcraft-handle-file
%{_datadir}/applications/leechcraft.desktop
%{_iconsdir}/hicolor/*/apps/leechcraft_main.png
%{_datadir}/%{name}/global_icons/
%{_datadir}/%{name}/qml/common
%{_datadir}/%{name}/qml/org
%{_datadir}/%{name}/settings/coresettings.xml
%{_datadir}/%{name}/sounds/
%{_datadir}/%{name}/themes/
%{_mandir}/man1/leechcraft.1*
%{_mandir}/man1/leechcraft-add-file.1*
%{_mandir}/man1/leechcraft-handle-file.1*

#----------------------------------------------------------------------------

%package plugins-main
Summary:	LeechCraft main modules
Group:		Networking/Other
Requires:	%{name} = %{EVRD}
Requires:	%{name}-advancednotifications = %{EVRD}
Requires:	%{name}-aggregator = %{EVRD}
Requires:	%{name}-azoth = %{EVRD}
Requires:	%{name}-bittorrent = %{EVRD}
Requires:	%{name}-lackman = %{EVRD}
Requires:	%{name}-lmp = %{EVRD}
Requires:	%{name}-monocle = %{EVRD}
Requires:	%{name}-poshuku = %{EVRD}

%description plugins-main
A meta-task to install LeechCraft key modules.

It selects following modules:
 * advancednotifications
 * aggregator
 * azoth
 * bittorrent
 * lackman
 * lmp
 * monocle
 * poshuku

Some other key modules are already selected by main LeechCraft package:
 * cstp
 * sb2
 * summary
 * tabsessmanager
 * tpi

%files plugins-main

#----------------------------------------------------------------------------

%package plugins-extra
Summary:	LeechCraft extra modules
Group:		Networking/Other
Requires:	%{name} = %{EVRD}
Requires:	%{name}-anhero = %{EVRD}
Requires:	%{name}-auscrie = %{EVRD}
Requires:	%{name}-blogique = %{EVRD}
Requires:	%{name}-dbusmanager = %{EVRD}
Requires:	%{name}-deadlyrics = %{EVRD}
Requires:	%{name}-dolozhee = %{EVRD}
Requires:	%{name}-gacts = %{EVRD}
Requires:	%{name}-glance = %{EVRD}
Requires:	%{name}-gmailnotifier = %{EVRD}
Requires:	%{name}-historyholder = %{EVRD}
Requires:	%{name}-hotsensors = %{EVRD}
Requires:	%{name}-hotstreams = %{EVRD}
Requires:	%{name}-kbswitch = %{EVRD}
Requires:	%{name}-kinotify = %{EVRD}
Requires:	%{name}-knowhow = %{EVRD}
Requires:	%{name}-lastfmscrobble = %{EVRD}
Requires:	%{name}-launchy = %{EVRD}
Requires:	%{name}-lemon = %{EVRD}
Requires:	%{name}-lhtr = %{EVRD}
Requires:	%{name}-liznoo = %{EVRD}
Requires:	%{name}-musiczombie = %{EVRD}
Requires:	%{name}-nacheku = %{EVRD}
Requires:	%{name}-netstoremanager = %{EVRD}
Requires:	%{name}-networkmonitor = %{EVRD}
Requires:	%{name}-newlife = %{EVRD}
Requires:	%{name}-otlozhu = %{EVRD}
Requires:	%{name}-pintab = %{EVRD}
Requires:	%{name}-pogooglue = %{EVRD}
Requires:	%{name}-secman = %{EVRD}
Requires:	%{name}-seekthru = %{EVRD}
Requires:	%{name}-shaitan = %{EVRD}
Requires:	%{name}-syncer = %{EVRD}
Requires:	%{name}-tabslist = %{EVRD}
Requires:	%{name}-touchstreams = %{EVRD}
Requires:	%{name}-vgrabber = %{EVRD}
Requires:	%{name}-vrooby = %{EVRD}
Requires:	%{name}-xproxy = %{EVRD}

%description plugins-extra
A meta-task to install LeechCraft additional modules.

It selects following modules:
 * anhero
 * auscrie
 * blogique
 * dbusmanager
 * deadlyrics
 * dolozhee
 * gacts
 * glance
 * gmailnotifier
 * historyholder
 * hotsensors
 * hotstreams
 * kbswitch
 * kinotify
 * knowhow
 * lastfmscrobble
 * launchy
 * lemon
 * lhtr
 * liznoo
 * musiczombie
 * nacheku
 * netstoremanager
 * networkmonitor
 * newlife
 * otlozhu
 * pintab
 * pogooglue
 * secman
 * seekthru
 * shaitan
 * syncer
 * tabslist
 * touchstreams
 * vgrabber
 * vrooby
 * xproxy

%files plugins-extra

#----------------------------------------------------------------------------

%define lcutil_major 0
%define liblcutil %mklibname lcutil %{lcutil_major}

%package -n %{liblcutil}
Summary:	LeechCraft shared library
Group:		System/Libraries

%description -n %{liblcutil}
LeechCraft shared library.

%files -n %{liblcutil}
%{_libdir}/liblcutil.so.%{lcutil_major}*

#----------------------------------------------------------------------------

%define xmlsettingsdialog_major 0
%define libxmlsettingsdialog %mklibname xmlsettingsdialog %{xmlsettingsdialog_major}

%package -n %{libxmlsettingsdialog}
Summary:	LeechCraft shared library
Group:		System/Libraries

%description -n %{libxmlsettingsdialog}
LeechCraft shared library.

%files -n %{libxmlsettingsdialog}
%{_libdir}/libxmlsettingsdialog.so.%{xmlsettingsdialog_major}*

#----------------------------------------------------------------------------

%package devel
Summary:	LeechCraft development files
Group:		Development/Other
Requires:	%{liblcutil} = %{EVRD}
Requires:	%{libxmlsettingsdialog} = %{EVRD}

%description devel
LeechCraft development files. Install them if you want to develop plugins.

%files devel
%{_libdir}/liblcutil.so
%{_libdir}/libxmlsettingsdialog.so
%{_includedir}/%{name}
%{_datadir}/cmake/Modules/InitLCPlugin.cmake
%{_datadir}/%{name}/cmake/

#----------------------------------------------------------------------------

%package advancednotifications
Summary:	LeechCraft Notifications framework module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description advancednotifications
This package provides an advanced notifications module for Leechcraft.

It's used for more flexible notifications customization.

%files advancednotifications -f leechcraft_advancednotifications.lang
%{_libdir}/%{name}/plugins/libleechcraft_advancednotifications*
%{_datadir}/%{name}/qml/advancednotifications
%{_datadir}/%{name}/settings/advancednotificationssettings.xml

#----------------------------------------------------------------------------

%package aggregator
Summary:	LeechCraft RSS/Atom Aggregator module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}
Requires:	%{name}-poshuku = %{EVRD}
Requires:	qt4-database-plugin-sqlite

%description aggregator
This package provides a RSS/Atom feed reader module for LeechCraft.

It features:
 * RSS 0.92/0.93/1.0/2.0, Atom 0.3/1.0;
 * extensions like GeoRSS, MediaRSS, Comment API etc;
 * OPML support;
 * broadcatching and fetching arbitrary data with regexps;
 * tape mode for news display;
 * individual options for each channel like update interval;
 * storage either in SQLite or PostgreSQL;
 * exporting feeds to FB2 for further reading on handheld devices.

%files aggregator -f leechcraft_aggregator.lang
%{_libdir}/%{name}/plugins/libleechcraft_aggregator*
%{_datadir}/%{name}/scripts/aggregator
%{_datadir}/%{name}/settings/aggregatorsettings.xml

#----------------------------------------------------------------------------

%package anhero
Summary:	LeechCraft Crash handler module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description anhero
This package provides a crash handler module for LeechCraft.

It uses KDE utils to handle crashes, show backtraces and aid
in sending bug reports.

KDE itself is not necessary to be running for AnHero to work.

%files anhero -f leechcraft_anhero.lang
%{_libdir}/%{name}/plugins/libleechcraft_anhero*

#----------------------------------------------------------------------------

%package auscrie
Summary:	LeechCraft screenshoter Module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description auscrie
This package provides a screenshooter module for LeechCraft.

It allows to make screenshots of LeechCraft and then either save them
locally or upload them to an imagebin.

%files auscrie -f leechcraft_auscrie.lang
%{_libdir}/%{name}/plugins/libleechcraft_auscrie*

#----------------------------------------------------------------------------

%package azoth
Summary:	Instant Messager client module for LeechCraft
Group:		Networking/Instant messaging
Requires:	%{name} = %{EVRD}

%description azoth
This package provides a modular IM client for LeechCraft.

Totally in the spirit of LeechCraft, Azoth is modular itself. For example,
protocols are provided by corresponding plugins, so Azoth is a multiprotocol
client as well. Modularity also allows Azoth to be flexible, extensible and
enables the modules to use each other and avoid code and functionality
duplication.

Unlike other multiprotocol clients which tend to implement only those
features that are present in all the protocols, Azoth is modelled after the
XMPP protocol, aiming to provide extensive and full support for XMPP while
remaining usable for other protocols.

%files azoth -f leechcraft_azoth.lang
%{_libdir}/%{name}/plugins/libleechcraft_azoth*
%{_datadir}/%{name}/azoth
%{_datadir}/applications/leechcraft-azoth-acetamide.desktop
%{_datadir}/applications/leechcraft-azoth-xoox.desktop
%{_datadir}/%{name}/settings/azoth*

#----------------------------------------------------------------------------

%package bittorrent
Summary:	LeechCraft BitTorrent client module
Group:		Networking/File transfer
Requires:	%{name} = %{EVRD}

%description bittorrent
This package provides a bittorrent client for LeechCraft.

It is feature-rich, fast and efficient.

Features
 * Support for DHT.
 * Magnet links support.
 * Sequential download mode where torrent is download sequentially.
 * Torrents queue, limiting number of seeding/leeching torrents.
 * Ability to rename files and directories in the torrent.
 * Selective download: possibility to select specific files from torrent.
 * Continue downloads left by any other client.
 * Support for sparse files.
 * Tags for torrents.
 * Global and per-torrent speed limits.
 * Connection number limits.
 * Fast resume support to avoid long startup times.
 * IP filter to block/unblock unwanted peers.
 * Support for extension protocol
etc.

%files bittorrent -f leechcraft_bittorrent.lang
%{_libdir}/%{name}/plugins/libleechcraft_bittorrent*
%{_datadir}/applications/leechcraft-bittorrent.desktop
%{_datadir}/%{name}/settings/torrentsettings.xml

#----------------------------------------------------------------------------

%package blogique
Summary:	LeechCraft blogging client module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}
Requires:	%{name}-lhtr = %{EVRD}

%description blogique
It supports different blogging platforms via different submodules.

Current sublodules are:
 * hestia, a local blogging platform
 * metida, a LiveJournal client

%files blogique -f leechcraft_blogique.lang
%{_libdir}/%{name}/plugins/libleechcraft_blogique.so
%{_libdir}/%{name}/plugins/libleechcraft_blogique_hestia.so
%{_libdir}/%{name}/plugins/libleechcraft_blogique_metida.so
%{_datadir}/%{name}/qml/blogique
%{_datadir}/%{name}/settings/blogique*

#----------------------------------------------------------------------------

%package cstp
Summary:	LeechCraft HTTP module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description cstp
This package provides HTTP implementation plugin for LeechCraft.

It is a clean and simple HTTP implementation. Mainly used by many other
plugins, like Aggregator or SeekThru or vGrabber.

Features:
 * Support for redirects.
 * Automatic downloads from other plugins.
 * Support for continuing of interrupted downloads.

%files cstp -f leechcraft_cstp.lang
%{_libdir}/%{name}/plugins/libleechcraft_cstp*
%{_datadir}/%{name}/settings/cstpsettings.xml

#----------------------------------------------------------------------------

%package dbusmanager
Summary:	LeechCraft D-Bus module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description dbusmanager
This package provides a D-Bus implementation module for LeechCraft.

It allows to use D-Bus. Currently, this only means showing notifications
via implementations supporting FreeDesktop's notifications standard,
like KDE 4.4 (or higher), Gnome, XFCE and others.

%files dbusmanager -f leechcraft_dbusmanager.lang
%{_libdir}/%{name}/plugins/libleechcraft_dbusmanager*
%{_datadir}/%{name}/settings/dbusmanagersettings.xml

#----------------------------------------------------------------------------

%package deadlyrics
Summary:	LeechCraft lyrics finder module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description deadlyrics
This package provides a lyrics finder module for LeechCraft.

It is a simple client for searching song lyrics on various sites.
The search interface is available via LeechCraft Summary.

%files deadlyrics -f leechcraft_deadlyrics.lang
%{_libdir}/%{name}/plugins/libleechcraft_deadlyrics*

#----------------------------------------------------------------------------

%package dolozhee
Summary:	LeechCraft issue reporting module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description dolozhee
This package provides a Dolozhee module for LeechCraft.

It allows to quickly and easily submit bug reports and feature
requests to LeechCraft issues tracker.

%files dolozhee -f leechcraft_dolozhee.lang
%{_libdir}/%{name}/plugins/libleechcraft_dolozhee*

#----------------------------------------------------------------------------

%package gacts
Summary:	LeechCraft global actions module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description gacts
This package provides a global shortcut manager for LeechCraft.

It allows to set and use global hotkeys.

%files gacts
%{_libdir}/%{name}/plugins/libleechcraft_gacts*

#----------------------------------------------------------------------------

%package glance
Summary:	LeechCraft opened tabs overview module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description glance
This package provides a tabs overview module for Leechcraft.

It allows to show the thumbnailed grid overview of tabs.


%files glance -f leechcraft_glance.lang
%{_libdir}/%{name}/plugins/libleechcraft_glance*

#----------------------------------------------------------------------------

%package gmailnotifier
Summary:	LeechCraft GMail notifier module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description gmailnotifier
This package provides a GMail notifications module for Leechcraft.

It allows to get notifications about new mail in your GMail account.

It has configurable frequency of the updates and the number of last unread
messages shown.

%files gmailnotifier -f leechcraft_gmailnotifier.lang
%{_libdir}/%{name}/plugins/libleechcraft_gmailnotifier*
%{_datadir}/%{name}/qml/gmailnotifier
%{_datadir}/%{name}/settings/gmailnotifiersettings.xml

#----------------------------------------------------------------------------

%package historyholder
Summary:	LeechCraft history module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description historyholder
This package provides a history keeper module for LeechCraft.

It allows to store information about finished downloads and similar events
and allows to search it by text, wildcard, regular expressions or tags.

%files historyholder -f leechcraft_historyholder.lang
%{_libdir}/%{name}/plugins/libleechcraft_historyholder*

#----------------------------------------------------------------------------

%package hotsensors
Summary:	LeechCraft temperature sensors module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description hotsensors
This package provides a temperature sensors module for LeechCraft.

%files hotsensors
%{_libdir}/%{name}/plugins/libleechcraft_hotsensors*
%{_datadir}/%{name}/qml/hotsensors

#----------------------------------------------------------------------------

%package hotstreams
Summary:	LeechCraft Radio streams module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}
Requires:	%{name}-lmp = %{EVRD}

%description hotstreams
This package provides a radio streams module for LeechCraft.

%files hotstreams
%{_libdir}/%{name}/plugins/libleechcraft_hotstreams*

#----------------------------------------------------------------------------

%package kbswitch
Summary:	LeechCraft keyboard switcher module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description kbswitch
This module allows to change keyboard layouts from LeechCraft.

%files kbswitch
%{_libdir}/%{name}/plugins/libleechcraft_kbswitch*
%{_datadir}/%{name}/settings/kbswitchsettings.xml

#----------------------------------------------------------------------------

%package kinotify
Summary:	LeechCraft kinetic notifications module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description kinotify
This package contains a fancy notifications module for LeechCraft.

It provides fancy kinetic notifications LeechCraft-wide instead of old-style
tray-based ones. It supports notifications with HTML markup, notification
actions (for example, "Open chat" action in a notification about incoming IM
message) and is fully themable.

Features:
 * Supports HTML markup.
 * Supports notification actions.
 * Themable.
 * Platform-independent.

%files kinotify -f leechcraft_kinotify.lang
%{_libdir}/%{name}/plugins/libleechcraft_kinotify*
%{_datadir}/%{name}/settings/kinotifysettings.xml
%{_datadir}/%{name}/kinotify/

#----------------------------------------------------------------------------

%package knowhow
Summary:	LeechCraft Tips of the day module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description knowhow
This package provides a tips module for LeechCraft.

It allows to display tips of the day window when LeechCraft starts.

%files knowhow
%{_libdir}/%{name}/plugins/libleechcraft_knowhow*
%{_datadir}/%{name}/settings/knowhowsettings.xml
%{_datadir}/%{name}/knowhow/

#----------------------------------------------------------------------------

%package lackman
Summary:	LeechCraft package manager module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description lackman
This package provides a package manager module for Leechcraft.

It allows to install script plugins, iconsets, translations, additional data
and other similar packages.

It also supports dependencies between packages as well as versioning and
automatic updates of the packages. LackMan works completely in userspace and
is crossplatform by its nature.

Features:
 * Allows installation of script plugins, icons and various other data.
 * Supports versioning and automatic updates of packages.
 * Supports dependencies between packages.
 * Works entirely in userspace, operating in user's home directory.
 * Is a crossplatform package manager.

%files lackman -f leechcraft_lackman.lang
%{_libdir}/%{name}/plugins/libleechcraft_lackman*
%{_datadir}/%{name}/settings/lackmansettings.xml

#----------------------------------------------------------------------------

%package lastfmscrobble
Summary:	LeechCraft Last.FM Scrobble module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}
Requires:	%{name}-lmp = %{EVRD}

%description lastfmscrobble
This package contains a LastFMScrobble module for LeechCraft.

It provides support for the Last.FM service. For example, it scrobble tracks
from other players, requests similar artists (on demand by other players as
well), supports fetching album art, etc.

Features:
 * Scrobbling listened tracks from other players like LMP to Last.FM.
 * "Loving" listened tracks.
 * Support for requesting artists that are similar to a given artist.
 * Automatic fetching of album art.
 * Support for Last.FM radio.
 * Fetching personalized recommendations.
 * Fetching recent releases of artists that are in the user's collection.
 * Fetching artists biography.
 * Configurable language of the fetched information.

%files lastfmscrobble -f leechcraft_lastfmscrobble.lang
%{_libdir}/%{name}/plugins/libleechcraft_lastfmscrobble*
%{_datadir}/%{name}/settings/lastfmscrobblesettings.xml

#----------------------------------------------------------------------------

%package launchy
Summary:	LeechCraft launcher module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description launchy
This package provides a third-party applications launcher module
for LeechCraft.

Features:
 * Support for favorites.
 * Quark for quickly opening applications added to favorites.
 * Keyboard navigation.
 * Filtering by application name, description or executable name.

%files launchy -f leechcraft_launchy.lang
%{_libdir}/%{name}/plugins/libleechcraft_launchy*
%{_datadir}/%{name}/qml/launchy

#----------------------------------------------------------------------------

%package lemon
Summary:	LeechCraft network monitor module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description lemon
This package provides another network monitor module for Leechcraft.

It provides a quark for panels like SB2 and traffic graphs.

%files lemon
%{_libdir}/%{name}/plugins/libleechcraft_lemon*
%{_datadir}/%{name}/qml/lemon

#----------------------------------------------------------------------------

%package lhtr
Summary:	LeechCraft HTML WYSIWYG editor module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description lhtr
This package provides a HTML WYSIWYG editor module for Leechcraft.

It can be usable with mail and blog modules.

%files lhtr -f leechcraft_lhtr.lang
%{_libdir}/%{name}/plugins/libleechcraft_lhtr*
%{_datadir}/%{name}/settings/lhtrsettings.xml

#----------------------------------------------------------------------------

%package liznoo
Summary:	LeechCraft power managment module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}
Requires:	upower

%description liznoo
This package provides a power manager plugin for Leechcraft.

It uses UPower on Linux.

Features:
 * Displays battery status in LeechCraft tray.
 * Displays battery charge and power consumption history.
 * Notifies other plugins about sleep and resume events. This way plugins
   like Azoth can disconnect from servers gracefully on hibernation and
   reconnect properly on startup.
 * Allows user to easily sleep/hibernate the system.
 * Notifies user when device starts discharging or charging.
 * Notifies user on low power level.

%files liznoo -f leechcraft_liznoo.lang
%{_libdir}/%{name}/plugins/libleechcraft_liznoo*
%{_datadir}/%{name}/settings/liznoosettings.xml

#----------------------------------------------------------------------------

%package lmp
Summary:	LeechCraft Media player module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}
Suggests:	%{name}-deadlyrics = %{EVRD}
Suggests:	%{name}-hotstreams = %{EVRD}
Suggests:	%{name}-lastfmscrobble = %{EVRD}
Suggests:	%{name}-musiczombie = %{EVRD}
Suggests:	%{name}-touchstreams = %{EVRD}

%description lmp
This package provides a audio player module for LeechCraft.

It allows to play audio and stream audio.
It uses Phonon as a backend thus supporting major codecs.

Features:
 * Support for major audio formats.
 * Streaming media over Internet.
 * Play queue.
 * Support for automatic podcast playing (with a plugin like Aggregator).

%files lmp -f leechcraft_lmp.lang
%{_libdir}/%{name}/plugins/libleechcraft_lmp*
%{_datadir}/%{name}/settings/lmp*

#----------------------------------------------------------------------------

%package monocle
Summary:	LeechCraft document viewer module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description monocle
This package provides a modular document viewer module for LeechCraft.

It supports different document formats via different backends.

Currently it has backends for:
 * PDF
 * PostScript
 * Djvu
 * FB2

%files monocle -f leechcraft_monocle.lang
%{_libdir}/%{name}/plugins/libleechcraft_monocle*
%{_datadir}/%{name}/settings/monoclesettings.xml
%{_datadir}/applications/leechcraft-monocle-fxb.desktop
%{_datadir}/applications/leechcraft-monocle-pdf.desktop
%{_datadir}/applications/leechcraft-monocle-postrus.desktop
%{_datadir}/applications/leechcraft-monocle-seen.desktop

#----------------------------------------------------------------------------

%package musiczombie
Summary:	LeechCraft MusicBrainz.org client module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}
Requires:	%{name}-lmp = %{EVRD}

%description musiczombie
This package provides a MusicBrainz.org client module for LeechCraft.

%files musiczombie
%{_libdir}/%{name}/plugins/libleechcraft_musiczombie*

#----------------------------------------------------------------------------

%package nacheku
Summary:	LeechCraft link watcher module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description nacheku
This package provides a Nacheku plugin for LeechCraft.

It allows to watch clipboard and directory in order to
get links and download files.

%files nacheku
%{_libdir}/%{name}/plugins/libleechcraft_nacheku*
%{_datadir}/%{name}/settings/nachekusettings.xml

#----------------------------------------------------------------------------

%package netstoremanager
Summary:	LeechCraft network file storages module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description netstoremanager
This package provides a network storage module for Leechcraft.

It allows to manage network storages like Google Drive.
It is modular, so different storages can be added to it
without modifying the plugin itself.

Features:
 * Upload files easily from LeechCraft.
 * Maintain the list of uploaded files.
 * Delete the uploaded files (if supported by service).
 * Support for prolongating uploaded files (if supported by service).

Supported services:
 * Google Drive
 * Yandex.Disk (currently disabled)

%files netstoremanager -f leechcraft_netstoremanager.lang
%{_libdir}/%{name}/plugins/libleechcraft_netstoremanager*
%{_datadir}/%{name}/settings/netstoremanagersettings.xml
%{_datadir}/%{name}/settings/nsmgoogledrivesettings.xml

#----------------------------------------------------------------------------

%package networkmonitor
Summary:	LeechCraft network monitor module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description networkmonitor
This package provides a network monitor module for LeechCraft.

It allows to watch for HTTP requests and allows to inspect them and search
through the list.

%files networkmonitor -f leechcraft_networkmonitor.lang
%{_libdir}/%{name}/plugins/libleechcraft_networkmonitor*

#----------------------------------------------------------------------------

%package newlife
Summary:	LeechCraft settings importer module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description newlife
This package provides a settings importer module for LeechCraft.

It allows to import settings, preferences etc. from various applications.

Currently it supports
 * Kopete: chat history.
 * Psi+: account settings, chat history.
 * Vacuum IM: account settings, chat history.
 * Akregator: feeds list, individual settings for each feed, like
   update interval and custom storage parameters, Akregator's settings.
 * Firefox: history, bookmarks, RSS feeds (aka Live bookmarks).
 * Liferea: feeds list.

%files newlife -f leechcraft_newlife.lang
%{_libdir}/%{name}/plugins/libleechcraft_newlife*

#----------------------------------------------------------------------------

%package otlozhu
Summary:	LeechCraft ToDo manager module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description otlozhu
This package provides a ToDo manager module for LeechCraft.

It is a GTD-inspired ToDo manager.

%files otlozhu -f leechcraft_otlozhu.lang
%{_libdir}/%{name}/plugins/libleechcraft_otlozhu*

#----------------------------------------------------------------------------

%package pintab
Summary:	LeechCraft pinning tabs module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description pintab
This package provides a pinning tabs module for LeechCraft.

It allows to pin important tabs so that they occupy less space.

%files pintab -f leechcraft_pintab.lang
%{_libdir}/%{name}/plugins/libleechcraft_pintab*

#----------------------------------------------------------------------------

%package pogooglue
Summary:	LeechCraft quick google search module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}
Requires:	%{name}-poshuku = %{EVRD}

%description pogooglue
This package provides a quick search module for LeechCraft.

It allows to search instantly selected text in Google.

%files pogooglue -f leechcraft_pogooglue.lang
%{_libdir}/%{name}/plugins/libleechcraft_pogooglue*

#----------------------------------------------------------------------------

%package poshuku
Summary:	Web Browser module for LeechCraft
Group:		Networking/WWW
Requires:	%{name} = %{EVRD}

%description poshuku
This package provides a full-featured WebKit-based Web Browser for LeechCraft.

%files poshuku -f leechcraft_poshuku.lang
%{_libdir}/%{name}/plugins/libleechcraft_poshuku*
%{_datadir}/%{name}/installed/poshuku
%{_datadir}/%{name}/settings/poshuku*

#----------------------------------------------------------------------------

%package sb2
Summary:	LeechCraft SideBar2 module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description sb2
This package provides another side bar module for Leechcraft.

It is a next-gen fluid sidebar with quick launch, tabs and tray areas.

%files sb2
%{_libdir}/%{name}/plugins/libleechcraft_sb2*
%{_datadir}/%{name}/qml/sb2

#----------------------------------------------------------------------------

%package secman
Summary:	LeechCraft security manager module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description secman
This package provides a security manager module for LeechCraft.

%files secman
%{_libdir}/%{name}/plugins/libleechcraft_secman*

#----------------------------------------------------------------------------

%package seekthru
Summary:	LeechCraft OpenSearch module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description seekthru
This package contains an OpenSearch module for LeechCraft.

It provides a search client for OpenSearch-enabled web sites and engines.

Features:
 * Support for autodiscovery of OpenSearch-capable web sites.
 * Tagging of search engines.
 * Support for queries to several search engines at once.
 * Support search results in RSS/Atom format and subscribe to them
   with a suitable plugin like Aggregator.
 * Show results in HTML format with a suitable plugin like Poshuku.

%files seekthru -f leechcraft_seekthru.lang
%{_libdir}/%{name}/plugins/libleechcraft_seekthru*
%{_datadir}/%{name}/settings/seekthrusettings.xml

#----------------------------------------------------------------------------

%package shaitan
Summary:	LeechCraft terminal module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}
Requires:	xterm

%description shaitan
This package provides a terminal module for LeechCraft, a wrapper over xterm.

%files shaitan
%{_libdir}/%{name}/plugins/libleechcraft_shaitan*

#----------------------------------------------------------------------------

%package summary
Summary:	LeechCraft summary info module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description summary
This package provides a summary module for LeechCraft.

It allows to show a quick overview of LeechCraft's state. It shows current
tasks like leeching or seeding torrents and downloading files with context-
dependent actions and views. It also can collect status information from
other plugins like unread channels.

Summary also allows to perform searches via the installed plugins
like SeekThru, HistoryHolder or vGrabber.

Features:
 * List of current tasks and events with context-dependent actions
   and views for selected items.
 * Support for gathering status information from other plugins.
 * Category-based search query support via other plugins.

%files summary -f leechcraft_summary.lang
%{_libdir}/%{name}/plugins/libleechcraft_summary*

#----------------------------------------------------------------------------

%package syncer
Summary:	LeechCraft synchronization module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description syncer
This package provides a synchronization module for LeechCraft.

It allows to synchronize data and settings between LeechCraft instances
running on different machines.

%files syncer -f leechcraft_syncer.lang
%{_libdir}/%{name}/plugins/libleechcraft_syncer*
%{_datadir}/%{name}/settings/syncersettings.xml

#----------------------------------------------------------------------------

%package tabsessmanager
Summary:	LeechCraft tab session manager module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description tabsessmanager
This package provides a Tab Session Manager module for LeechCraft.

TabSessManager allows to restore automatically last session and
allows to create named sessions.

Features:
 * Automatically restores last session on LeechCraft startup.
 * Allows one to save named sessions for restoring them later.

%files tabsessmanager -f leechcraft_tabsessmanager.lang
%{_libdir}/%{name}/plugins/libleechcraft_tabsessmanager*

#----------------------------------------------------------------------------

%package tabslist
Summary:	LeechCraft tabs list module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description tabslist
This package provides a tabs list module for Leechcraft.

It allows to show the list of currently opened tabs and allows to quickly
navigate between them.

%files tabslist -f leechcraft_tabslist.lang
%{_libdir}/%{name}/plugins/libleechcraft_tabslist*

#----------------------------------------------------------------------------

%package touchstreams
Summary:	LeechCraft VK.com client module for audio streaming
Group:		Networking/Other
Requires:	%{name} = %{EVRD}
Requires:	%{name}-lmp = %{EVRD}

%description touchstreams
This package provides a VK.com client module for LeechCraft.

TouchStreams is used for streaming audio from this social network.
It allows other plugins like LMP to query for available tracks given artist
name, track name or a free-form string and returns the tracks available for
streaming.

%files touchstreams -f leechcraft_touchstreams.lang
%{_libdir}/%{name}/plugins/libleechcraft_touchstreams*
%{_datadir}/%{name}/settings/touchstreamssettings.xml

#----------------------------------------------------------------------------

%package tpi
Summary:	LeechCraft task progress indicator module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description tpi
This package provides a task progress indicator quark module for LeechCraft.

%files tpi
%{_libdir}/%{name}/plugins/libleechcraft_tpi*
%{_datadir}/%{name}/qml/tpi

#----------------------------------------------------------------------------

%package vgrabber
Summary:	LeechCraft Vkontakte grabber module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description vgrabber
This package provides a Vkontakte.ru module for LeechCraft.

It allows to grab and play audio and video from the russian
social network Vkontakte.

Features:
 * Download or stream audios and videos from Vkontakte.
 * Search for audios and videos.

%files vgrabber -f leechcraft_vgrabber.lang
%{_libdir}/%{name}/plugins/libleechcraft_vgrabber*
%{_datadir}/%{name}/settings/vgrabbersettings.xml

#----------------------------------------------------------------------------

%package vrooby
Summary:	LeechCraft removable storage devices manager module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}
Requires:	udisks

%description vrooby
This package provides a removable storage devices manager module
for LeechCraft.

It allows to watch removable storage devices via d-bus and udisks.

%files vrooby -f leechcraft_vrooby.lang
%{_libdir}/%{name}/plugins/libleechcraft_vrooby*

#----------------------------------------------------------------------------

%package xproxy
Summary:	LeechCraft proxy manager module
Group:		Networking/Other
Requires:	%{name} = %{EVRD}

%description xproxy
This package provides an advanced proxy manager module for LeechCraft.

It allows to configure and use proxy servers.

%files xproxy -f leechcraft_xproxy.lang
%{_libdir}/%{name}/plugins/libleechcraft_xproxy*
%{_datadir}/%{name}/settings/xproxysettings.xml

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%global optflags %{optflags} -O0
pushd src
%cmake \
	-DENABLE_LADS:BOOL=OFF \
	-DENABLE_QROSP:BOOL=OFF
%make
popd

%install
pushd src
%makeinstall_std -C build
popd

%find_lang %{name} --with-qt
%find_lang leechcraft_advancednotifications --with-qt
%find_lang leechcraft_aggregator --with-qt
%find_lang leechcraft_anhero --with-qt
%find_lang leechcraft_auscrie --with-qt
%find_lang leechcraft_azoth \
		leechcraft_azoth_acetamide \
		leechcraft_azoth_autoidler \
		leechcraft_azoth_autopaste \
		leechcraft_azoth_birthdaynotifier \
		leechcraft_azoth_chathistory \
		leechcraft_azoth_depester \
		leechcraft_azoth_herbicide \
		leechcraft_azoth_hili  \
		leechcraft_azoth_isterique \
		leechcraft_azoth_lastseen \
		leechcraft_azoth_metacontacts \
		leechcraft_azoth_modnok \
		leechcraft_azoth_p100q \
		leechcraft_azoth_rosenthal \
		leechcraft_azoth_vader \
		leechcraft_azoth_xoox \
		leechcraft_azoth_xtazy \
		leechcraft_azoth.lang --with-qt
%find_lang leechcraft_bittorrent --with-qt
%find_lang leechcraft_blogique --with-qt
%find_lang leechcraft_cstp --with-qt
%find_lang leechcraft_dbusmanager --with-qt
%find_lang leechcraft_deadlyrics --with-qt
%find_lang leechcraft_dolozhee --with-qt
%find_lang leechcraft_glance --with-qt
%find_lang leechcraft_gmailnotifier --with-qt
%find_lang leechcraft_historyholder --with-qt
%find_lang leechcraft_kinotify --with-qt
%find_lang leechcraft_lackman --with-qt
%find_lang leechcraft_lastfmscrobble --with-qt
%find_lang leechcraft_launchy --with-qt
%find_lang leechcraft_lhtr --with-qt
%find_lang leechcraft_liznoo --with-qt
%find_lang leechcraft_lmp \
		leechcraft_lmp_dumbsync \
		leechcraft_lmp_graffiti \
		leechcraft_lmp.lang --with-qt
%find_lang leechcraft_monocle --with-qt
%find_lang leechcraft_netstoremanager \
		leechcraft_netstoremanager_googledrive \
		leechcraft_netstoremanager.lang --with-qt
%find_lang leechcraft_networkmonitor --with-qt
%find_lang leechcraft_newlife --with-qt
%find_lang leechcraft_otlozhu --with-qt
%find_lang leechcraft_pintab --with-qt
%find_lang leechcraft_pogooglue --with-qt
%find_lang leechcraft_poshuku \
		leechcraft_poshuku_cleanweb \
		leechcraft_poshuku_fatape \
		leechcraft_poshuku_filescheme \
		leechcraft_poshuku_fua \
		leechcraft_poshuku_onlinebookmarks \
		leechcraft_poshuku_onlinebookmarks_delicious \
		leechcraft_poshuku_onlinebookmarks_readitlater \
		leechcraft_poshuku.lang --with-qt
%find_lang leechcraft_seekthru --with-qt
%find_lang leechcraft_summary --with-qt
%find_lang leechcraft_syncer --with-qt
%find_lang leechcraft_tabsessmanager --with-qt
%find_lang leechcraft_tabslist --with-qt
%find_lang leechcraft_touchstreams --with-qt
%find_lang leechcraft_vgrabber --with-qt
%find_lang leechcraft_vrooby --with-qt
%find_lang leechcraft_xproxy --with-qt

