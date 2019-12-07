import scala.collection.mutable
import scala.io.Source
import scala.util.Using

object Main1 {
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
    var totalOrbits = 0
    objects.values.foreach(v => {
      totalOrbits += traceOrbits(v)
    })
    println("orbits: " + totalOrbits)
  }

  def traceOrbits(v: Vertex): Int = {
    if (v.orbitsAround.isDefined) {
      return traceOrbits(v.orbitsAround.get) + 1
    }
    0
  }

  class Vertex(var orbitsAround: Option[Vertex]) {

  }
}
