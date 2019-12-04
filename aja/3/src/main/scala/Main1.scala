import scala.collection.mutable
import scala.io.Source
import scala.util.Using
import scala.math.{min,max}

object Main1 {
  def main(args: Array[String]): Unit = {
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
    var grid = Array.ofDim[Boolean](xMax + 1 - xMin,yMax + 1 - yMin)
    val intersections = new mutable.HashSet[(Int,Int)]
    Using(Source.fromFile(args(0))) {
      source => {
        val inputLines = source.getLines()
        execLineOfCommands(start,inputLines.next().split(","),(i,j) => {
          grid = grid.updated(i,grid(i).updated(j,true))
        })
        execLineOfCommands(start,inputLines.next().split(","),(i,j) => {
          if (grid(i)(j)) {
            intersections += ((i,j))
          }
        })
      }
    }
    shortestDistance(start,intersections)
  }

  def execLineOfCommands(start: (Int,Int), commands: Array[String], func: (Int,Int) => Unit): Unit = {
    var pos = start
    commands.foreach {
      command => {
        val diff = parseCommand(command)
        (min(pos._1 + 1, pos._1 + diff._1) to max(pos._1 + diff._1, pos._1 - 1)).foreach {
          i =>
            (min(pos._2 + 1, pos._2 + diff._2) to max(pos._2 + diff._2, pos._2 - 1)).foreach {
              j => {
                func(i,j)
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

  def shortestDistance(central: (Int,Int), intersections: mutable.HashSet[(Int,Int)]): Unit = {
    var lowest = Int.MaxValue
    intersections.foreach {
      i => {
        val distance = (central._1 - i._1).abs + (central._2 - i._2).abs
        if (distance < lowest) {
          lowest = distance
        }
      }
    }
    println(lowest)
  }
}
