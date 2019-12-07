import scala.collection.mutable
import scala.io.Source
import scala.util.Using

object Main2 {
  def main(args: Array[String]): Unit = {
    val objects = new mutable.HashMap[String,Vertex]()
    Using(Source.fromFile(args(0))) {
      source =>
        source.getLines().foreach {
          line => {
            val orbitObjects = line.split(')')
            if (objects.contains(orbitObjects(0))) {
              if (objects.contains(orbitObjects(1))) {
                objects(orbitObjects(1)).orbitsAround = Some(objects(orbitObjects(0)))
              } else {
                objects.put(orbitObjects(1),new Vertex(Some(objects(orbitObjects(0)))))
              }
            } else {
              objects.put(orbitObjects(0),new Vertex(None))
              if (objects.contains(orbitObjects(1))) {
                objects(orbitObjects(1)).orbitsAround = Some(objects(orbitObjects(0)))
              } else {
                objects.put(orbitObjects(1),new Vertex(Some(objects(orbitObjects(0)))))
              }
            }
          }
        }
    }
    println(findSanta(objects))
  }

  def traceOrbits(v: Vertex): Int = {
    if (v.orbitsAround.isDefined) {
      return traceOrbits(v.orbitsAround.get) + 1
    }
    0
  }

  def findSanta(objects: mutable.HashMap[String,Vertex]): Int = {
    var santaPath = List((0,objects("SAN").orbitsAround.get))
    var youPath = List((0,objects("YOU").orbitsAround.get))

    var lengthAndMaybeVertex = santaPath.last
    while (lengthAndMaybeVertex._2.orbitsAround.isDefined) {
      santaPath = santaPath.appended(lengthAndMaybeVertex._1+1,lengthAndMaybeVertex._2.orbitsAround.get)
      lengthAndMaybeVertex = santaPath.last
    }
    lengthAndMaybeVertex = youPath.last
    while (lengthAndMaybeVertex._2.orbitsAround.isDefined) {
      santaPath.foreach(lv => {
        if (lengthAndMaybeVertex._2 == lv._2) {
          return lengthAndMaybeVertex._1 + lv._1
        }
      })
      youPath = youPath.appended(lengthAndMaybeVertex._1+1,lengthAndMaybeVertex._2.orbitsAround.get)
      lengthAndMaybeVertex = youPath.last
    }
    Int.MaxValue
  }

  class Vertex(var orbitsAround: Option[Vertex]) {

  }
}
