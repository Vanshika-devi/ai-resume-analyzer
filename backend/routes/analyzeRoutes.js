import express from 'express'

import upload from '../utils/upload.js'

import protect from '../middleware/authMiddleware.js'

import {

    analyzeResume,

} from '../controllers/analyzeController.js'

const router = express.Router()

router.post(

    '/resume',

    protect,

    upload.single('resume'),

    analyzeResume
)

export default router