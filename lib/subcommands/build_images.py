# Copyright (C) IBM Corp. 2016.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging

from lib import iso_builder

LOG = logging.getLogger(__name__)


def run(CONF):
    build_iso = CONF.get('iso')

    if build_iso:
        builder = iso_builder.MockPungiIsoBuilder(CONF)
        builder.build()
        builder.clean()
        LOG.info("ISO built succesfully")
    else:
        LOG.info("--iso was not specified, nothing to do here")
