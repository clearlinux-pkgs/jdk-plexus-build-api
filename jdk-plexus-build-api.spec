Name     : jdk-plexus-build-api
Version  : 0.0.7
Release  : 1
URL      : https://github.com/sonatype/sisu-build-api/archive/plexus-build-api-0.0.7.tar.gz
Source0  : https://github.com/sonatype/sisu-build-api/archive/plexus-build-api-0.0.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : apache-maven
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-wagon
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn
Buildrequires : jdk-spice-parent
Buildrequires : jdk-forge-parent
Buildrequires : jdk-maven-javadoc-plugin
Buildrequires : jdk-maven-jar-plugin
Buildrequires : jdk-maven-resources-plugin
Buildrequires : jdk-maven-compiler-plugin
Buildrequires : jdk-surefire
Buildrequires : jdk-xbean
Buildrequires : jdk-maven-filtering
Buildrequires : jdk-maven-shared-utils
Buildrequires : jdk-plexus-build-api
Buildrequires : jdk-maven-shared-utils
Buildrequires : jdk-maven-plugin-tools
Buildrequires : jdk-maven-shared-incremental
Buildrequires : jdk-plexus-compiler
Buildrequires : jdk-plexus-interactivity
Buildrequires : jdk-maven-reporting-api
Buildrequires : jdk-maven-archiver
Buildrequires : jdk-maven-invoker
Buildrequires : jdk-maven-common-artifact-filters
Buildrequires : jdk-doxia
Buildrequires : jdk-doxia-sitetools
Buildrequires : jdk-plexus-archiver
Buildrequires : jdk-plexus-io
Buildrequires : jdk-commons-compress
Buildrequires : jdk-snappy-java
Buildrequires : jdk-xmlunit
Buildrequires : jdk-plexus-i18n
Buildrequires : jdk-plexus-velocity
Buildrequires : jdk-velocity
Buildrequires : jdk-commons-collections
Buildrequires : jdk-log4j
Buildrequires : apache-maven2
Buildrequires : jdk-qdox
Buildrequires : jdk-jdom
Buildrequires : jdk-plexus-cli
Patch1: plexus-build-api-migration-to-component-metadata.patch

%description
No detailed description available

%prep
%setup -q -n sisu-build-api-plexus-build-api-0.0.7
%patch1 -p1

python3 /usr/share/java-utils/mvn_file.py : plexus/plexus-build-api

%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n plexus-build-api -d %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/java/plexus/plexus-build-api.jar
/usr/share/maven-metadata/plexus-build-api.xml
/usr/share/maven-poms/plexus/plexus-build-api.pom
