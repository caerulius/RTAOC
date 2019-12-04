import scala.collection.mutable
import scala.io.Source
import scala.util.Using
import scala.math.{min,max}

object Main2 {
  def maain(args: Array[String]): Unit = {
    var xMin = 0
    var yMin = 0
    var xMax = 0
    var yMax = 0
    Using(Source.fromFile(args(0))) {
      source => source.getLines().foreach {
        line => {
          var pos = (0,0)
          for (command <- line.split(",")) {
            val diff = parseCommand(command)
            pos = (pos._1 + diff._1,pos._2 + diff._2)
            if (pos._1 > xMax) {
              xMax = pos._1
            }
            if (pos._1 < xMin) {
              xMin = pos._1
            }
            if (pos._2 > yMax) {
              yMax = pos._2
            }
            if (pos._2 < yMin) {
              yMin = pos._2
            }
          }
        }
      }
    }
    val start = (0 - xMin, 0 - yMin)
    var pos = start
    var traveledDistance = 0
    var grid = Array.ofDim[Int](xMax + 1 - xMin,yMax + 1 - yMin)
    val intersections = new mutable.HashSet[Int]
    Using(Source.fromFile(args(0))) {
      source => {
        val inputLines = source.getLines()
        execLineOfCommands(start,inputLines.next().split(","),(i,j,traveledDistance) => {
          grid = grid.updated(i,grid(i).updated(j,traveledDistance))
        })
        execLineOfCommands(start,inputLines.next().split(","), (i,j,traveledDistance) => {
          if (grid(i)(j) > 0) {
            intersections += grid(i)(j) + traveledDistance
          }
        })
      }
    }
    println(intersections.min)
  }

  def execLineOfCommands(start: (Int,Int), commands: Array[String], func: (Int,Int,Int) => Unit): Unit = {
    var pos = start
    var traveledDistance = 0
    commands.foreach {
      command => {
        val diff = parseCommand(command)
        val xRange = if (diff._1 < 0)
          (min(pos._1 + 1, pos._1 + diff._1) to max(pos._1 + diff._1, pos._1 - 1)).reverse
        else
          min(pos._1 + 1, pos._1 + diff._1) to max(pos._1 + diff._1, pos._1 - 1)
        xRange.foreach {
          i =>
            val yRange = if (diff._2 < 0)
              (min(pos._2 + 1, pos._2 + diff._2) to max(pos._2 + diff._2, pos._2 - 1)).reverse
            else
              min(pos._2 + 1, pos._2 + diff._2) to max(pos._2 + diff._2, pos._2 - 1)
            yRange.foreach {
              j => {
                traveledDistance += 1
                func(i,j,traveledDistance)
              }
            }
        }
        pos = (pos._1 + diff._1, pos._2 + diff._2)
      }
    }
  }

  def parseCommand(command: String): (Int,Int) = {
    command.charAt(0) match {
      case 'R' =>
        (command.substring(1).toInt,0)
      case 'L' =>
        (-command.substring(1).toInt,0)
      case 'U' =>
        (0,-command.substring(1).toInt)
      case 'D' =>
        (0,command.substring(1).toInt)
      case _ =>
        println(command)
        (0,0)
    }
  }
}