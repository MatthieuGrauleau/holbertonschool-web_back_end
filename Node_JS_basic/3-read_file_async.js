const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf-8');
    const lines = data.trim().split('\n').filter((line) => line);
    const headers = lines[0].split(',');
    const students = lines.slice(1);

    if (students.length === 0) {
      throw new Error('No students found');
    }

    console.log(`Number of students: ${students.length}`);

    const fields = {};
    students.forEach((student) => {
      const studentInfo = student.split(',');
      const field = studentInfo[headers.indexOf('field')];
      const firstName = studentInfo[headers.indexOf('firstname')];

      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstName);
    });

    for (const [field, studentsList] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${studentsList.length}. List: ${studentsList.join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
