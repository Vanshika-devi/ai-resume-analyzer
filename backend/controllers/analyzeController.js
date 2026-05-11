import fs from 'fs'

import pdf from 'pdf-parse/lib/pdf-parse.js'

import Resume from '../models/Resume.js'

import calculateATS from '../services/atsService.js'

const analyzeResume = async (req, res) => {

    try {

        const dataBuffer =
            fs.readFileSync(req.file.path)

        const pdfData =
            await pdf(dataBuffer)

        const atsScore =
            calculateATS(pdfData.text)

        const feedback =
            atsScore > 70
                ? 'Strong Resume'
                : 'Needs Improvement'

        const resume =
            await Resume.create({

                user: req.user.id,

                fileName:
                    req.file.filename,

                atsScore,

                feedback,
            })

        res.status(200).json({

            atsScore,

            feedback,

            resume,
        })

    } catch (error) {

        console.log(error)

        res.status(500).json({

            message: error.message,
        })
    }
}

export {

    analyzeResume,
}