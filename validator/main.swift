import Foundation
let data = try Data(contentsOf: URL(fileURLWithPath: CommandLine.arguments[1]))
_ = try CourseBundle.decode(data)
print("Course Bundle valid")
