#!/bin/sh
# ----------------------------------------------------------------------------
#  Copyright 2001-2006 The Apache Software Foundation.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# ----------------------------------------------------------------------------

#   Copyright (c) 2001-2002 The Apache Software Foundation.  All rights
#   reserved.

BASEDIR=`dirname $0`/..
BASEDIR=`(cd "$BASEDIR"; pwd)`



# OS specific support.  $var _must_ be set to either true or false.
cygwin=false;
darwin=false;
case "`uname`" in
  CYGWIN*) cygwin=true ;;
  Darwin*) darwin=true
           if [ -z "$JAVA_VERSION" ] ; then
             JAVA_VERSION="CurrentJDK"
           else
             echo "Using Java version: $JAVA_VERSION"
           fi
           if [ -z "$JAVA_HOME" ] ; then
             JAVA_HOME=/System/Library/Frameworks/JavaVM.framework/Versions/${JAVA_VERSION}/Home
           fi
           ;;
esac

if [ -z "$JAVA_HOME" ] ; then
  if [ -r /etc/gentoo-release ] ; then
    JAVA_HOME=`java-config --jre-home`
  fi
fi

# For Cygwin, ensure paths are in UNIX format before anything is touched
if $cygwin ; then
  [ -n "$JAVA_HOME" ] && JAVA_HOME=`cygpath --unix "$JAVA_HOME"`
  [ -n "$CLASSPATH" ] && CLASSPATH=`cygpath --path --unix "$CLASSPATH"`
fi

# If a specific java binary isn't specified search for the standard 'java' binary
if [ -z "$JAVACMD" ] ; then
  if [ -n "$JAVA_HOME"  ] ; then
    if [ -x "$JAVA_HOME/jre/sh/java" ] ; then
      # IBM's JDK on AIX uses strange locations for the executables
      JAVACMD="$JAVA_HOME/jre/sh/java"
    else
      JAVACMD="$JAVA_HOME/bin/java"
    fi
  else
    JAVACMD=`which java`
  fi
fi

if [ ! -x "$JAVACMD" ] ; then
  echo "Error: JAVA_HOME is not defined correctly."
  echo "  We cannot execute $JAVACMD"
  exit 1
fi

if [ -z "$REPO" ]
then
  REPO="$BASEDIR"/lib
fi

CLASSPATH=$CLASSPATH_PREFIX:"$BASEDIR"/conf:"$REPO"/sekiro-business-api-1.4.jar:"$REPO"/sekiro-netty-1.0.1.jar:"$REPO"/jctools-core-1.2.1.jar:"$REPO"/sekiro-netty-codec-http-1.0.0.jar:"$REPO"/guava-29.0-jre.jar:"$REPO"/failureaccess-1.0.1.jar:"$REPO"/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar:"$REPO"/jsr305-3.0.2.jar:"$REPO"/checker-qual-2.11.1.jar:"$REPO"/error_prone_annotations-2.3.4.jar:"$REPO"/j2objc-annotations-1.3.jar:"$REPO"/commons-lang3-3.12.0.jar:"$REPO"/commons-io-2.8.0.jar:"$REPO"/slf4j-api-1.7.30.jar:"$REPO"/logback-core-1.2.3.jar:"$REPO"/logback-classic-1.2.3.jar:"$REPO"/lombok-1.18.20.jar:"$REPO"/sekiro-service-demo-0.0.1.jar
EXTRA_JVM_ARGUMENTS="-Xms1024m -Xmx1024m -XX:NewSize=512m"

# For Cygwin, switch paths to Windows format before running java
if $cygwin; then
  [ -n "$CLASSPATH" ] && CLASSPATH=`cygpath --path --windows "$CLASSPATH"`
  [ -n "$JAVA_HOME" ] && JAVA_HOME=`cygpath --path --windows "$JAVA_HOME"`
  [ -n "$HOME" ] && HOME=`cygpath --path --windows "$HOME"`
  [ -n "$BASEDIR" ] && BASEDIR=`cygpath --path --windows "$BASEDIR"`
  [ -n "$REPO" ] && REPO=`cygpath --path --windows "$REPO"`
fi

exec "$JAVACMD" $JAVA_OPTS \
  $EXTRA_JVM_ARGUMENTS \
  -classpath "$CLASSPATH" \
  -Dapp.name="sekiro" \
  -Dapp.pid="$$" \
  -Dapp.repo="$REPO" \
  -Dbasedir="$BASEDIR" \
  com.virjar.sekiro.business.netty.Bootstrap \
  "$@"
