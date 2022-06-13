#!/usr/bin/python3
#
# Copyright 2021 David SPORN
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from DatasheetUtils import pinIndex
from ChipSymbolUnit import ChipSymbolUnit

class PinsOrganizerMultiUnit:
    """
    Collection of utility functions to generate a ChipSymbolUnit for a unit from a multi-unit symbol.

    It should be used when unit per unit.

    Two strategies are available :
    * single group unit : pins are on the left and the right of the symbol, depending on their direction ; the sorting is
        done by pin number, except buses that are sorted from MSB to LSB, if recognised.
    * power unit : power pins are appended on the left, and ground pins are appended on the right ; each pin is between
        spacers .

    To accomodate each unit, and given that there will be no pin on the top of the surface, the annotations (title, reference,
    subtitle) will be horizontally centered, and the surface top coordinate will be zeroself.

    Then the rendering of the multi unit is following :
    * render the global annotations (for each line, compute the halfWidth, the text is rendered at x = -halfWidth)
    * for each group (rank >= 0) : render the subtitle (again centered with x = -halfWidth of the line) ; organize the
        pins of the group, render the chip translated by -halfHeight
    * render the power unit : special subtitle (again centered with x = -halfWidth of the line) ; organize the pins of
        the group, render the chip translated by -halfHeight 

    """

    @staticmethod
    def organizeSingleGroup(group):
        ##HERE
        ##TO DO

    @staticmethod
    def organizePowerUnit(pwrGroup, gndGroup):
        ##HERE
        ##TO DO


    @staticmethod
    def organizeIntoBoard(datasheet):
        sortedPins=sorted(datasheet['pins'],key=pinIndex)

        halfLength=int(len(sortedPins) / 2)

        leftPins=sortedPins[0:halfLength]
        rightPins=sortedPins[halfLength:len(sortedPins)]

        result=ChipSymbolUnit()
        result.appendVertically(leftPins,rightPins)
        return result

    @staticmethod
    def organizeIntoDip(datasheet):
        sortedPins=sorted(datasheet['pins'],key=pinIndex)

        halfLength=int(len(sortedPins) / 2)

        leftPins=sortedPins[0:halfLength]
        rightPins=list(reversed(sortedPins[halfLength:len(sortedPins)]))

        result=ChipSymbolUnit()
        result.appendVertically(leftPins,rightPins)
        return result

    @staticmethod
    def organizeIntoQfp(datasheet):
        sortedPins=sorted(datasheet['pins'],key=pinIndex)

        sideLength=int(len(sortedPins)/4)

        leftPins=sortedPins[0:sideLength]
        bottomPins=sortedPins[sideLength:2*sideLength]
        rightPins=list(reversed(sortedPins[2*sideLength:3*sideLength]))
        topPins=list(reversed(sortedPins[3*sideLength:len(sortedPins)]))

        result=ChipSymbolUnit()
        result.appendVertically(leftPins,rightPins)
        result.appendHorizontally(topPins,bottomPins)
        return result


    @staticmethod
    def organizeIntoLcc(datasheet):
        sortedPins=sorted(datasheet['pins'],key=pinIndex)

        sideLength=int(len(sortedPins)/4)
        deltaLeft=int(sideLength/2) + 1


        leftPins=sortedPins[deltaLeft:deltaLeft+sideLength]
        bottomPins=sortedPins[deltaLeft+sideLength:deltaLeft+2*sideLength]
        rightPins=list(reversed(sortedPins[deltaLeft+2*sideLength:deltaLeft+3*sideLength]))
        topPins=list(reversed(sortedPins[deltaLeft+3*sideLength:len(sortedPins)]+sortedPins[0:deltaLeft]))

        result=ChipSymbolUnit()
        result.appendVertically(leftPins,rightPins)
        result.appendHorizontally(topPins,bottomPins)
        return result

    @staticmethod
    def organizeIntoSimm(datasheet):
        sortedPins=sorted(datasheet['pins'],key=pinIndex)

        result=ChipSymbolUnit()
        result.appendVertically(sortedPins,[])
        return result

    @staticmethod
    def organizeIntoDimm(datasheet):
        sortedPins=sorted(datasheet['pins'],key=pinIndex)

        leftPins=sortedPins[0::2]
        rightPins=sortedPins[1::2]
        result=ChipSymbolUnit()
        result.appendVertically(leftPins,rightPins)
        return result
